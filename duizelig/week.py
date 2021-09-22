w = 1
d = input('dag: ')
if d == 'ma':
    d = 2
elif d == 'di':
    d = 3
elif d == 'wo':
    d = 4
elif d == 'do':
    d = 5
elif d == 'vr':
    d = 6
elif d == 'za':
    d = 7
elif d == 'zo':
    d = 8

while w != d:
    if w == 1:
        print('maandag')
    elif w == 2:
        print('dinsdag')
    elif w == 3:
        print('woensdag')
    elif w == 4:
        print('donderdag')
    elif w == 5:
        print('vrijdag')
    elif w == 6:
        print('zaterdag')
    elif w == 7:
        print('zondag')
    w = w + 1