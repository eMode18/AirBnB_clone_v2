#!/usr/bin/python3
"""A Fabric script to create and distribute an archive
to web servers, based on  the deploy function"""
import os
from datetime import datetime
from fabric.api import *

env.hosts = ['100.26.173.127', '100.26.209.143']


def do_pack():
    """Create compressed archive from contents of web_static directory"""
    local("mkdir -p versions")
    archive_file = 'versions/web_static_{}.tgz'.format(
        datetime.strftime(datetime.now(), "%Y%m%d%I%M%S"))
    compression_cmd = 'tar -cvzf {} web_static'.format(archive_file)
    tar_command = local(compression_cmd)
    if tar_command.failed:
        return None
    else:
        return archive_file


def do_deploy(archive_path):
    """Deploy an archive to web servers"""
    if not os.path.exists(archive_path):
        return False
    archive_name = archive_path.split('/')[1]
    folder_name = archive_name.split('.')[0]
    upload_result = put(archive_path, '/tmp/{}'.format(archive_name))
    if upload_result.failed:
        return False
    create_release_dir = run(
        'mkdir -p /data/web_static/releases/{}'.format(folder_name))
    if create_release_dir.failed:
        return False
    extract_archive = run(
        'tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
        .format(archive_name, folder_name))
    if extract_archive.failed:
        return False
    remove_tmp_archive = run('rm /tmp/{}'.format(archive_name))
    if remove_tmp_archive.failed:
        return False
    move_files_cmd = 'mv /data/web_static/releases/{0}/web_static/* ' \
                     '/data/web_static/releases/{0}/'.format(folder_name)
    move_files_result = run(move_files_cmd)
    if move_files_result.failed:
        return False
    remove_old_web_static = run(
        'rm -rf /data/web_static/releases/{}/web_static'.format(folder_name))
    if remove_old_web_static.failed:
        return False
    remove_current_symlink = run('rm -rf /data/web_static/current')
    if remove_current_symlink.failed:
        return False
    create_new_symlink = run(
        'ln -s /data/web_static/releases/{}/ /data/web_static/current'
        .format(folder_name))
    if create_new_symlink.failed:
        return False
    print('New version deployed!')
    return True


def deploy():
    """Create and distribute an archive to web servers using deploy function"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    deployment_result = do_deploy(archive_path)
    return deployment_result
