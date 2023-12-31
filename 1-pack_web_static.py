#!/usr/bin/python3
"""This script generates a .tgz archive from the
web_static folder's content  of your AirBnB Clone repo, using
a cunstom function do_pack"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Compress the contents of web_static into the archive"""
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    archive_name = "web_static_{}.tgz".format(timestamp)
    result = local("tar -cvzf versions/{} web_static".format(archive_name))
    if result.succeeded:
        return "versions/{}".format(archive_name)
    else:
        return None
