#!/usr/bin/python3
"""
a script that deletes out-of-date archives
fab -f 100-clean_web_static.py do_clean:number=2
    -i ssh-key -u ubuntu > /dev/null 2>&1
"""

from fabric.api import *
import os

env.hosts = ['54.157.157.93', '54.167.173.197']


def do_clean(number=0):
    """a func that deletes out-of-date archives.
    Args:
        number (int): The number of archives to keep.
    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [ab for ab in archives if "web_static_" in ab]
        [archives.pop() for ix in range(number)]
        [run("rm -rf ./{}".format(ab)) for ab in archives]
