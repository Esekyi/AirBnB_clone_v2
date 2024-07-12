#!/usr/bin/python3
"""a Fabric script that generates a .tgz archive from the contents of the web_static"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """generates a .tgz archive from the contents of the web_static"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f'web_static_{date}.tgz'
    if not os.path.exists("versions"):
        os.makedirs("versions")
    local('tar -cvzf versions/{} web_static'.format(archive_name))
    archive_path = "versions/" + archive_name
    if os.path.exists(archive_path):
        return archive_path
    else:
        return None
