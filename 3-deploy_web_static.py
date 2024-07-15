#!/usr/bin/python3
"""
Fabric script to deploy an archived files to a remote server
"""

from fabric.api import env, put, run, local
import os
# import sys
from datetime import datetime


env.hosts = [
    '100.26.211.53',
    '34.229.70.70'
]

env.user = 'ubuntu'
# env.key = '~/.ssh/id_rsa'


def do_pack():
    """
    do_pack Function
    generates a .tgz archive from the contents of the web_static
    """
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


def do_deploy(archive_path):
    """
    do_deploy Function
    Deploy an archived files to a remote server
    @archive_path: path to the archives
    """
    if not os.path.isfile(archive_path):
        return False

    try:
        split_path = archive_path.split('/')
        filename = split_path[-1]
        file_name = filename.split('.')[0]
        print("Executing task 'do_deploy'")
        put(archive_path, '/tmp/')
        run('mkdir -p /data/web_static/releases/{}'.format(file_name))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'
            .format(filename, file_name))
        run('rm /tmp/{}'.format(filename))
        run("""mv /data/web_static/releases/{}/web_static/*
             /data/web_static/releases/{}/"""
            .format(file_name, file_name))
        run('rm -rf /data/web_static/releases/{}/web_static'
            .format(file_name))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{} /data/web_static/current'
            .format(file_name))
        return True
    except Exception as e:
        return False


def deploy():
    """
    Deploy function
    Packs and make the full deployment
    """
    packed_package = do_pack()
    if not packed_package:
        return False
    return do_deploy(packed_package)
