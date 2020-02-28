import sys

from common import *
from const import *

dialog = Dialog('print')
player = sys.argv[0].split('.', 1)[0]
socket, aes = setup(player, BUFFER_DIR, BUFFER_FILE_NAME)

dialog.info("Waiting for message...")
received = receive_and_decrypt(aes, socket)
dialog.chat('Alice said: "{}"'.format(received))
if CUSTOM_CHAT:
    dialog.prompt('Please input message...')
    to_send = input()
else:
    if received == NICE_MSG['alice']:
        to_send = NICE_MSG[player]
    elif received == BAD_MSG['alice']:
        to_send = BAD_MSG[player]
    else:
        to_send = 'What?!'
encrypt_and_send(to_send, aes, socket)
dialog.info('Message sent!')

tear_down(socket, BUFFER_DIR, BUFFER_FILE_NAME)
