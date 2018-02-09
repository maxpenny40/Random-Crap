# Caeser Cipher v1

string1 = 'dylanfarrer'

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

encrypted = []

shift = 1

s = 0


string1 = list(string1)

while s < len(string1):
    a = 0
    while a < 26:
        if string1[s] == alphabet[a]:
            if alphabet[a] == 'w':
                shift = -25
            if alphabet[a] == 'x':
                shift = -25
            elif alphabet[a] == 'y':
                shift = -25
            elif alphabet[a] == 'z':
                shift = -25
            encrypted.append(alphabet[shift+a])
        a += 1
    s += 1

print(string1)
print(encrypted)