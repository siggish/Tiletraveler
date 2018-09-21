#Starting tile is 1.1
#you can move north south east west.
#if there is a wall you cant move in that direction
#There are nine tiles, 3x3.
#When you get to tile 3,1 you win.



x = 1

y = 1

print('You can travel: (N)orth.')

while True:
    if x == 1 and y == 1:
        direction_a = input('Direction: ')
        direction = direction_a.lower()
        if direction == 'n':
            y = y + 1
            print('You can travel: (N)orth or (E)ast or (S)outh.')
        if direction == 's':
            print('Not a valid direction!')
        if direction == 'e':
            print('Not a valid direction!')
        if direction == 'w':
            print('Not a valid direction!')
            
    if x == 1 and y == 2:
        direction_a = input('Direction: ')
        direction = direction_a.lower()
        if direction == 'n':
            y = y + 1
            print('You can travel: (E)ast or (S)outh.')
        if direction == 's':
            y = y - 1
            print('You can travel: (N)orth.')
        if direction == 'e':
            x = x + 1
            print('You can travel: (S)outh or (W)est.')
        if direction == 'w':
            print('Not a valid direction!')

    if x == 1 and y == 3:
        direction_a = input('Direction: ')
        direction = direction_a.lower()
        if direction == 'n':
            print('Not a valid direction!')
        if direction == 's':
            y = y - 1
            print('You can travel: (N)orth or (E)ast or (S)outh.')
        if direction == 'e':
            x = x + 1
            print('You can travel: (E)ast or (W)est.')
        if direction == 'w':
            print('Not a valid direction!')


    if x == 2 and y == 1:
        direction_a = input('Direction: ')
        direction = direction_a.lower()
        if direction == 'n':
            y = y + 1
            print('You can travel: (S)outh or (W)est.')
        if direction == 's':
            print('Not a valid direction!') 
        if direction == 'e':
            print('Not a valid direction!') 
        if direction == 'w':
            print('Not a valid direction!')

    

    if x == 2 and y == 2:
        direction_a = input('Direction: ')
        direction = direction_a.lower()
        if direction == 'n':
            print('Not a valid direction!') 
        if direction == 's':
            y = y - 1
            print('You can travel: (N)orth.')
        if direction == 'e':
            print('Not a valid direction!') 
        if direction == 'w':
            x = x - 1
            print('You can travel: (N)orth or (E)ast or (S)outh.')
            


    if x == 2 and y == 3:
        direction_a = input('Direction: ')
        direction = direction_a.lower()
        if direction == 'n':
            print('Not a valid direction!') 
        if direction == 's':
            print('Not a valid direction!') 
        if direction == 'e':
            x = x + 1
            print('You can travel: (S)outh or (W)est.')
        if direction == 'w':
            x = x - 1
            print('You can travel: (S)outh or (E)ast.')
        


    if x == 3 and y == 2:
        direction_a = input('Direction: ')
        direction = direction_a.lower()
        if direction == 'n':
            y = y + 1
            print('You can travel: (S)outh or (W)est.')
        if direction == 's':
            y = y - 1
            print('Victory!')
            break
        if direction == 'e':
            print('Not a valid direction!') 
        if direction == 'w':
            print('Not a valid direction!')


    if x == 3 and y == 3:
        direction_a = input('Direction: ')
        direction = direction_a.lower()
        if direction == 'n':
            print('Not a valid direction!') 
        if direction == 's':
            y = y - 1
            print('You can travel: (N)orth or (S)outh.')
        if direction == 'e':
            print('Not a valid direction!') 
        if direction == 'w':
            x = x - 1
            print('You can travel: (E)ast or (W)est.')
        












