message = input("enter your message:")
private_key = input("enter your private key:")

sorted_pk = sorted(private_key)
order = []
for letter in private_key:
    position = sorted_pk.index(letter)
    # mark as read incase of duplicate characters in key
    sorted_pk[position] = ''
    order.append(position)
