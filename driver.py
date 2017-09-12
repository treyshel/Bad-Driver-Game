import random
import itertools


class Driver:
    ''' class for driver game '''

    def __init__(self, width, height, roadwidth):
        ''' (int, int, int) -> '''
        self.width = width
        self.height = height
        self.roadwidth = roadwidth
        left = (width - roadwidth) // 2
        right = width - left - roadwidth
        self.grid = [(left, roadwidth, right) for _ in range(height)]
        self.alive = True
        self.car = (width // 2 - 1, 2)
        self.score = 0
        self.level = 1

    def __str__(self):
        ''' returns string version of grid '''
        s = 'LEVEL: {} 🚁 HELI-ESCAPE 🚁 SCORE: {}'.format(
            self.level, self.score).center(self.width)
        s += '\n'
        slice_top = self.grid[:(-self.car[1])]
        _car = self.grid[(-self.car[1])]
        slice_bottom = self.grid[(-self.car[1]):]

        for line in slice_top:
            s += 'I{}^{}^{}I\n'.format(line[0] * '.', line[1] * ' ',
                                       line[2] * '.')

        l = self.car[0] - _car[0] - 1
        r = _car[1] - l - 2
        c = '{}🚁{}'.format(' ' * l, ' ' * r)
        s += 'I{}^{}^{}I\n'.format(_car[0] * '.', c, _car[2] * '.')

        for line in slice_bottom:
            s += 'I{}^{}^{}I\n'.format(line[0] * '.', line[1] * ' ',
                                       line[2] * '.')
        return s

    def game_update(self, key):
        ''' updates the grid with a new value and removes old value 
        returns self to completely update the state
        '''
        x, y = self.car
        if key == 'left':
            x -= 1
        elif key == 'right':
            x += 1
        elif key == 'up':
            y = min(y + 1, self.height - 2)
        elif key == 'down':
            y = max(y - 1, 2)
        self.car = (x, y)
        self.score += 1
        if not (self.score % 100):
            self.level += 1
            self.roadwidth -= 1
        self.grid.pop()
        move = random.choice((-1, 0, 1))
        l, rw, r = self.grid[0]
        left = l + move
        right = self.width - left - self.roadwidth
        if left >= 0 and right >= 0:
            self.grid.insert(0, (left, self.roadwidth, right))
        else:
            self.grid.insert(0, (l, rw, r))
        return self

    def keep_going(self):
        ''' Driver -> Bool
        Function will see if the car is hitting the edge or if it is
        '''
        x, y = self.car
        l, road, r = self.grid[-y]
        return x > l and x < (l + road)
