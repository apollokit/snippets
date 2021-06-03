from collections import namedtuple

KBCntrlCommand = namedtuple('KBCntrlCommand', 'name payload')

payload = 12
cmd = KBCntrlCommand('command', payload)