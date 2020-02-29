import sys
import os

from common import *
from const import *

dialog = Dialog('print')
player = sys.argv[0].split('.', 1)[0]
flag = sys.argv[1]
# whenever Bob sends a message, read it in 'buffer_original'
# Connect with Bob and perform DHKE
socket_bob, aes = setup('alice', BUFFER_DIR, BUFFER_FILE_NAME)

dialog.think('Eve thinks: "Nice, getting there..."')
os.rename(os.path.join(BUFFER_DIR, BUFFER_FILE_NAME), os.path.join(BUFFER_DIR, 'buffer_original'))
# Open new socket for Alice and perform DHKE
socket_alice, aes = setup('bob', BUFFER_DIR, BUFFER_FILE_NAME)
dialog.think('Eve thinks: "Hehe, it\'s working!"')

if flag == "--relay":
    # No MitM attack
    from_Alice = receive_and_decrypt(aes, socket_alice)
    dialog.chat('Alice slurred: "{}"'.format(from_Alice))
    encrypt_and_send(from_Alice, aes, socket_bob)

    from_Bob = receive_and_decrypt(aes, socket_bob)
    dialog.chat('Bob slurred: "{}"'.format(from_Bob))
    encrypt_and_send(from_Bob, aes, socket_alice)
elif flag == "--break-heart":
    # Change messages
    from_Alice = receive_and_decrypt(aes, socket_alice)
    dialog.chat('Alice slurred: "{}"'.format(from_Alice))
    to_Bob = 'I hate you!'   
    encrypt_and_send(to_Bob, aes, socket_bob)

    from_Bob = receive_and_decrypt(aes, socket_bob)
    dialog.chat('Bob slurred: "{}"'.format(from_Bob))
    to_Alice = 'You broke my heart...'
    encrypt_and_send(to_Alice, aes, socket_alice)
elif flag == "--custom":
    # User input a message to terminal
    from_Alice = receive_and_decrypt(aes, socket_alice)
    dialog.chat('Alice slurred: "{}"'.format(from_Alice))
    dialog.think('Input what you would like Alice to say to Bob')
    to_Bob = input()
    encrypt_and_send(to_Bob, aes, socket_bob)

    from_Bob = receive_and_decrypt(aes, socket_bob)
    dialog.chat('Bob slurred: "{}"'.format(from_Bob))
    dialog.think('Input what you would like Bob to say to Alice')
    to_Bob = input()
    encrypt_and_send(from_Bob, aes, socket_alice)
# else:
#     raise

# Close the two sockets
tear_down(socket_bob, BUFFER_DIR, 'buffer_original')
tear_down(socket_alice, BUFFER_DIR, BUFFER_FILE_NAME)


## info: yellow, chat: green, 