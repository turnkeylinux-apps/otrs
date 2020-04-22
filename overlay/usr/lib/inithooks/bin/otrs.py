#!/usr/bin/python3
"""Set OTRS admin password

Option:
    --pass=     unless provided, will ask interactively

"""

import sys
import getopt
import shlex
import inithooks_cache
import re

from dialog_wrapper import Dialog
import subprocess

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
    email = ""
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--pass':
            password = val

    if not password:
        d = Dialog('TurnKey Linux - First boot configuration')
        password = d.get_password(
            "OTRS Password",
            "Enter new password for the OTRS 'admin' account.")

    if not email:
        if 'd' not in locals():
            d = Dialog('Turnkey Linux - First boot configuration')
        
        email = d.get_email(
            "OTRS Email",
            "Enter email address for the OTRS 'admin' account.",
            "admin@example.com")

    inithooks_cache.write('APP_EMAIL', email)

    quoted_password = shlex.quote(password)
    subprocess.run(['su', '-c',
        f'/usr/share/otrs/bin/otrs.Console.pl Admin::User::SetPassword root@localhost {quoted_password}',
        '-s', '/bin/bash', 'otrs'])
    
    lines = []
    with open('/etc/otrs/cron', 'r') as fob:
        for line in fob:
            lines.append(re.sub(
                r'^MAILTO=".*"\s*$',
                'MAILTO={}'.format(shlex.quote(email)),
                line))
    with open('/etc/otrs/cron', 'w') as fob:
        fob.writelines(lines)

if __name__ == "__main__":
    main()

