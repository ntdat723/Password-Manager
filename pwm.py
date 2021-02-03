#! python3
import sys
import pyperclip


password = { # ex: '<nametag1>': 'password1',
              'email': 'abcdefgh'
            }

if len(sys.argv) < 2:
    print('Usage: python pwm.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in password:
    pyperclip.copy(password[account])
    print('Password has been copied into clipboard.')
else:
    print('No password for ' + account)
