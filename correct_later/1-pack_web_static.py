#!/usr/bin/python3
"""
A Fabric script to genereate .tgz archive
execute: fab -f 1-pack_web_static.py do_pack
"""

from datetime import datetime
from fabric.api import *


def do_pack():
    """
    a func that makes an archive on web_static folder
    """

    cur_time = datetime.now()
    archv = 'web_static_' + cur_time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    make = local('tar -cvzf versions/{} web_static'.format(archv))
    if make is not None:
        return archve
    else:
        return None
