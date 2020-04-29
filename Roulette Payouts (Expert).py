from random import randrange
i = randrange(-1, 37)

black_spaces = [2, 4, 6, 8, 10, 11, 13, 15, 17,
                20, 22, 24, 26, 28, 29, 31, 33, 35]
red_spaces = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19,
              21, 23, 25, 27, 30, 32, 34, 36]
color = []
ode = []
size = []

if -2 < i < 1:
    if i == 0:
        print("""
The spin result in 0...
Pay 0""")
    if i == -1:
        print("""
The spin result in 00...
Pay 00""")
else:
    if i in black_spaces:
        color = ['Black']
        if i % 2 == 1:
            ode = ['Odd']
            if 1 <= i <= 18:
                size = ['1 to 18']
            else:
                size = ['19 to 36']
        elif i % 2 == 0:
            ode = ['Even']
            if 1 <= i <= 18:
                size = ['1 to 18']
            else:
                size = ['19 to 36']
    elif i in red_spaces:
        color = ['Red']
        if i % 2 == 1:
            ode = ['Odd']
            if 1 <= i <= 18:
                size = ['1 to 18']
            else:
                size = ['19 to 36']
        elif i % 2 == 0:
            ode = ['Even']
            if 1 <= i <= 18:
                size = ['1 to 18']
            else:
                size = ['19 to 36']

    print(f'''
the spin resulted in {i}...
Pay {i}
Pay {color[0]}
Pay {ode[0]}
Pay {size[0]}
    ''')