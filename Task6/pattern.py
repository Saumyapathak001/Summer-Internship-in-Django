rows = 5
for i in range(1, rows + 1):
    print('* ' * i)

rows = 5
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '* ' * i)

rows = 5
for i in range(rows, 0, -1):
    print('* ' * i)


rows = 5
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '* ' * (2 * i - 1))



rows = 5
for i in range(1, rows + 1):
    if i == 1:
        print(' ' * (rows - i) + '*')
    else:
        print(' ' * (rows - i) + '*' + ' ' * (2 * (i - 1) - 1) + '*')
for i in range(rows - 1, 0, -1):
    if i == 1:
        print(' ' * (rows - i) + '*')
    else:
        print(' ' * (rows - i) + '*' + ' ' * (2 * (i - 1) - 1) + '*')



rows = 5
for i in range(1, rows + 1):
    if i == rows:
        print('* ' * (2 * i - 1))
    else:
        print(' ' * (rows - i) + '*' + ' ' * (2 * i - 3) + '*' if i > 1 else ' ' * (rows - i) + '*')



rows = 5
for i in range(rows):
    if i == 0 or i == rows - 1:
        print('* ' * rows)
    else:
        print('* ' + '  ' * (rows - 2) + '*')


rows = 5
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '* ' * (2 * i - 1))
for i in range(rows - 1, 0, -1):
    print(' ' * (rows - i) + '* ' * (2 * i - 1))
 