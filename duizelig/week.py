dag = 'start'
day = input('What day is it?: ')

while dag != day:
    if dag == 'start':
        print('ma')
        dag = 'ma'
    elif dag == 'ma':
        print('di')
        dag = 'di'
    elif dag == 'di':
        print('wo')
        dag = 'wo'
    elif dag == 'wo':
        print('do')
        dag = 'do'
    elif dag == 'do':
        print('vr')
        dag = 'vr'
    elif dag == 'vr':
        print('za')
        dag = 'za'
    elif dag == 'za':
        print('zo')
        dag = 'zo'