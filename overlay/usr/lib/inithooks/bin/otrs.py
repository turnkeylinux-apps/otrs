#!/usr/bin/python3
"""Set OTRS admin ('root@localhost') password

Option:
    --pass=     unless provided, will ask interactively

"""

import sys
import getopt
import shlex
import re
import subprocess

from libinithooks.dialog_wrapper import Dialog

def usage(s=None):
    if s:
        print("Error:", s, file=sys.stderr)
    print("Syntax: %s [options]" % sys.argv[0], file=sys.stderr)
    print(__doc__, file=sys.stderr)
    sys.exit(1)

def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h", ['help', 'pass=', 'email='])
    except getopt.GetoptError as e:
        usage(e)

    password = ""
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--pass':
            password = val

    if not password:
        d = Dialog('TurnKey Linux - First boot configuration')
        password = d.get_password(
            "OTRS Password",
            "Enter new password for the OTRS 'root@localhost' account.")

    quoted_password = shlex.quote(password)
    subprocess.run(['su', '-c',
        f'LC_ALL=C.UTF-8 /usr/share/otrs/bin/otrs.Console.pl Admin::User::SetPassword root@localhost {quoted_password}',
        '-s', '/bin/bash', 'otrs'])
    
if __name__ == "__main__":
    main()
