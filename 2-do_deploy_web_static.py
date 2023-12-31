#!/usr/bin/python3
"""this script distributes an archive to your web servers"""
from fabric.api import env, put, run
import os

env.hosts = ['100.26.173.127', '100.26.209.143']


def do_deploy(archive_path):
    """Perform the deployment"""
    if not os.path.exists(archive_path):
        return False

    try:
        archive_name = archive_path.split('/')[-1]
        folder_name = archive_name.split('.')[0]
        put(archive_path, '/tmp/')
        run('mkdir -p /data/web_static/releases/{}/'.format(folder_name))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
            .format(archive_name, folder_name))
        run('rm /tmp/{}'.format(archive_name))
        run('mv /data/web_static/releases/{}/web_static/* \
                /data/web_static/releases/{}/'
            .format(folder_name, folder_name))
        run('rm -rf /data/web_static/releases/{}/web_static'
            .format(folder_name))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(folder_name))
        print("New version deployed!")
        return True
    except Exception as e:
        return False
