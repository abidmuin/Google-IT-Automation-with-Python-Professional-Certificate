#!/usr/bin/env python

import subprocess
# ! Have to insert "/home/username/" before "/data/prod" and "/data/prod_backup/"
src = "/home/student-03-c93d9bf39303/data/prod/"
dest = "/home/student-03-c93d9bf39303/data/prod_backup/"
subprocess.call(["rsync", "-arq", src, dest])
