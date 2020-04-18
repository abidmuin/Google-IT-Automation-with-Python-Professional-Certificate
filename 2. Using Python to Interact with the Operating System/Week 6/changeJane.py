#!/usr/bin/env python3

import sys
import subprocess

with open(sys.argv[1], "r") as f:
    for reader in f.readlines():
        oldName = reader.strip()
        newName = oldName.replace("jane", "jdoe")
        subprocess.run(["mv", oldName, newName])
