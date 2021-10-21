def encode(message, key):
    acc = ""
    for c in message:
        i = ord(c)
        k = key + i
        c = chr(k)
        acc = acc + c
    return acc


def encode_better(message, key):
    acc = ""
    for i in range(len(message)):
        c = message[i]
        k = key[i % len(key)]
        c = ord(c)
        k = ord(k) - 97
        c = chr(c + k)
        acc = acc + c
    return acc