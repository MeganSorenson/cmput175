# input message and private key
message = input("enter your message:")
private_key = input("enter your private key:")

# sort private key and compare to private key
# determine position of each character of private key in sorted key
sorted_pk = sorted(private_key)
order = []
for letter in private_key:
    position = sorted_pk.index(letter)
    # mark as read incase of duplicate characters in key
    sorted_pk[position] = ''
    order.append(position)

# make the length of the message a multiple of the length of the order
while (len(message) % len(order) != 0):
    message = message + ' '

# copy message in chunks the size of order into a list to get a list of snips
i = 0
snips = []
while i < len(message):
    snip = message[i:i+len(order)]
    snips.append(snip)
    i += len(order)

# iterate to take the ith character of each snip
# in the list of snips following the order from phase 2 and
# form a new Message using a separator
cipher = ''
for i in range(len(order)):
    position = order.index(i)
    for snip in snips:
        cipher = cipher + snip[position]
    cipher += '#'

# print the new message
print(cipher)
