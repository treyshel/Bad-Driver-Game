import random
import itertools


class Driver:
    ''' class for driver game '''

    def __init__(self, grid):
        ''' (Grid) -> '''
        self.alive = True
        self.car = width // 2
        self.score = 0
        self.grid = grid


class Grid:
    '''  class to make the map for the car to drive on '''

    def __init__(self, width, height, roadwidth):
        ''' (int, int) -> '''
        self.width = width
        self.height = height
        self.roadwidth = roadwidth
        left = (width - roadwidth) // 2
        right = width - left - roadwidth
        self.posns = [(left, roadwidth, right) for _ in range(height)]

    def __str__(self):
        ''' returns string version of grid '''
        s = ''
        for line in self.posns:
            s += 'I{}^{}^{}I\n'.format(line[0] * '.', line[1] * ' ',
                                       line[2] * '.')
        # take this part out later
        x, rw, _ = self.posns[-1]
        x = x + (rw // 2) + 1
        s += '{}:0:'.format(x * ' ')
        return s

    def update(self):
        ' updates the grid with a new value and removes old value '
        self.posns.pop()
        move = random.choice((-1, 0, 1))
        l, rw, r = self.posns[0]
        left = l + move
        right = self.width - left - self.roadwidth
        if left >= 0 and right >= 0:
            self.posns.insert(0, (left, self.roadwidth, right))
        else:
            self.posns.insert(0, (l, rw, r))


def initial_state(width, height):
    return {
        'alive': True,
        'car': [(0, 0)],
        'score': 0,
        'width': width,
        'height': height,
        'direction': 'right'
    }


# def new_head_pos(state, dx, dy):
#     snake = state['snake']
#     head_x = state['width'] - 1 if snake[0][0] + dx < 0 else (
#         snake[0][0] + dx) % state['width']
#     head_y = state['height'] - 1 if snake[0][1] + dy < 0 else (
#         snake[0][1] + dy) % state['height']
#     return head_x, head_y

# def movement_from(direction):
#     if direction == 'left':
#         dx, dy = -1, 0
#     elif direction == 'right':
#         dx, dy = 1, 0

#     return dx, dy

# def move(state, direction):
#     dx, dy = movement_from(direction)
#     head_pos = new_head_pos(state, dx, dy)

#     if is_on_apple(state['snake'][0][0], state['snake'][0][1],
#                    state['apple'][0], state['apple'][1]):
#         state['snake'] = [head_pos] + state['snake']
#         state['score'] += len(state['snake'])
#         new_apple(state)
#     else:
#         state['snake'] = [head_pos] + state['snake'][:-1]

#     return state

# def is_crash(head_x, head_y, apple_x, apple_y):
#     '''(Int, Int, Int, Int) -> Bool

#     Returns Tru

#     >>> is_on_apple(4, 3, 4, 3)
#     True
#     >>> is_on_apple(0, 1, 1, 0)
#     False
#     >>> is_on_apple(1, 1, 1, 1)
#     True
#     >>> is_on_apple(1, 2, 3, 4)
#     False
#     >>> is_on_apple(0, 1, 0, 1)
#     True
#     >>> is_on_apple(0, 2, 0, 1)
#     False
#     >>> is_on_apple(2, 0, 1, 0)
#     False
#     '''
#     if (head_x == apple_x) and (head_y == apple_y):
#         return True

#     else:
#         return False

# def change_direction(current_direction, new_direction):
#     ''' (String, String) -> String

#     Returns the next direction the snake should be heading.
#     If the new direction would turn the snake completely around,
#     the old direction is maintained.

#     >>> change_direction('left', 'right')
#     'left'
#     >>> change_direction('right', 'left')
#     'right'
#     '''
#     if current_direction == 'left' and new_direction == 'right':
#         return current_direction
#     elif current_direction == 'right' and new_direction == 'left':
#         return current_direction

# def update(state, action):
#     if action == 'restart':
#         return initial_state(state['width'], state['height'])
#     if state['alive']:
#         if is_on_self(state):
#             state['alive'] = False
#             return state
#         elif action == 'tick':
#             return move(state, state['direction'])
#         else:
#             state['direction'] = change_direction(state['direction'], action)
#             return state
#     else:
#         return state