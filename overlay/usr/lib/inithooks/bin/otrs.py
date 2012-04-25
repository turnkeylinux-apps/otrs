#!/usr/bin/python
"""Set OTRS admin password

Option:
    --pass=     unless provided, will ask interactively

"""

import sys
import getopt
import crypt

from dialog_wrapper import Dialog
from mysqlconf import MySQL

def usage(s=None):
    if s:
        print >> sys.stderr, "Error:", s
    print >> sys.stderr, "Syntax: %s [options]" % sys.argv[0]
    print >> sys.stderr, __doc__
    sys.exit(1)

def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h", ['help', 'pass='])
    except getopt.GetoptError, e:
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
            "Enter new password for the OTRS 'admin' account.")

    hashpass = crypt.crypt(password, 'ro')

    m = MySQL()
    m.execute('UPDATE otrs2.users SET pw=\"%s\" WHERE login=\"admin\";' % hashpass)

if __name__ == "__main__":
    main()

