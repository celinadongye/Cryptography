import sys
import os

from common import *
from const import *

dialog = Dialog('print')
player = sys.argv[0].split('.', 1)[0]
flag = sys.argv[1]

# Connect with Bob and perform DHKE
socket_bob, aes_bob = setup('alice', BUFFER_DIR, BUFFER_FILE_NAME)
dialog.think('Eve thinks: "Nice, getting there..."')

# Rename buffer file to avoid race conditions
os.rename(os.path.join(BUFFER_DIR, BUFFER_FILE_NAME), os.path.join(BUFFER_DIR, 'buffer_original'))

# Open new socket for Alice and perform DHKE
socket_alice, aes_alice = setup('bob', BUFFER_DIR, BUFFER_FILE_NAME)
dialog.think('Eve thinks: "Hehe, it\'s working!"')

# No MitM attack
if flag == "--relay":
    # Decrypt message from Alice, encrypt and send it to Bob
    from_Alice = receive_and_decrypt(aes_alice, socket_alice)
    dialog.chat('Alice slurred: "{}"'.format(from_Alice))
    encrypt_and_send(from_Alice, aes_bob, socket_bob)
    # Decrypt response from Bob, encrypt and send it to Alice
    from_Bob = receive_and_decrypt(aes_bob, socket_bob)
    dialog.chat('Bob slurred: "{}"'.format(from_Bob))
    encrypt_and_send(from_Bob, aes_alice, socket_alice)

# Change messages
elif flag == "--break-heart":
    # Decrypt message from Alice, encrypt hate message and send it to Bob
    from_Alice = receive_and_decrypt(aes_alice, socket_alice)
    dialog.chat('Alice slurred: "{}"'.format(from_Alice))
    to_Bob = 'I hate you!'   
    encrypt_and_send(to_Bob, aes_bob, socket_bob)
    # Decrypt response from Bob, encrypt and send it to Alice
    from_Bob = receive_and_decrypt(aes_bob, socket_bob)
    dialog.chat('Bob slurred: "{}"'.format(from_Bob))
    encrypt_and_send(from_Bob, aes_alice, socket_alice)

# Prompt user to input message to terminal
elif flag == "--custom":
    # Decrypt message from Alice, encrypt user inputted message and send it to Bob
    from_Alice = receive_and_decrypt(aes_alice, socket_alice)
    dialog.chat('Alice slurred: "{}"'.format(from_Alice))
    dialog.think('Input what you would like Alice to say to Bob')
    to_Bob = input()
    encrypt_and_send(to_Bob, aes_bob, socket_bob)
    # Decrypt response from Alice, encrypt user inputted message and send it to Alice
    from_Bob = receive_and_decrypt(aes_bob, socket_bob)
    dialog.chat('Bob slurred: "{}"'.format(from_Bob))
    dialog.think('Input what you would like Bob to say to Alice')
    to_Bob = input()
    encrypt_and_send(from_Bob, aes_alice, socket_alice)

# Close the two sockets (with Alice and Bob)
tear_down(socket_bob, BUFFER_DIR, 'buffer_original')
tear_down(socket_alice, BUFFER_DIR, BUFFER_FILE_NAME)