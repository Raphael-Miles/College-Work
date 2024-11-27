
import random

def grid():
    for _ in range(4):
        print('0 ' * 4)
    

def update_grid():
    ui = input('Press E to start or X to exit')
    while True:
        if ui == 'X':
            break
        else:
            grid()
    
update_grid()