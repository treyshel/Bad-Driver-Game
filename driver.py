import random
import itertools


def initial_state(width, height):
    return {
        'alive': True,
        'snake': [(0, 0)],
        'apple': (random.randrange(1, width), random.randrange(1, height)),
        'score': 0,
        'width': width,
        'height': height,
        'direction': 'right'
    }


def new_head_pos(state, dx, dy):
    snake = state['snake']
    head_x = state['width'] - 1 if snake[0][0] + dx < 0 else (
        snake[0][0] + dx) % state['width']
    head_y = state['height'] - 1 if snake[0][1] + dy < 0 else (
        snake[0][1] + dy) % state['height']
    return head_x, head_y


def movement_from(direction):
    if direction == 'left':
        dx, dy = -1, 0
    elif direction == 'right':
        dx, dy = 1, 0
    elif direction == 'up':
        dx, dy = 0, -1
    elif direction == 'down':
        dx, dy = 0, 1

    return dx, dy


def move(state, direction):
    dx, dy = movement_from(direction)
    head_pos = new_head_pos(state, dx, dy)

    if is_on_apple(state['snake'][0][0], state['snake'][0][1],
                   state['apple'][0], state['apple'][1]):
        state['snake'] = [head_pos] + state['snake']
        state['score'] += len(state['snake'])
        new_apple(state)
    else:
        state['snake'] = [head_pos] + state['snake'][:-1]

    return state


def is_on_apple(head_x, head_y, apple_x, apple_y):
    '''(Int, Int, Int, Int) -> Bool

    Returns True if the snake's head is on the apple.

    >>> is_on_apple(4, 3, 4, 3)
    True
    >>> is_on_apple(0, 1, 1, 0)
    False
    >>> is_on_apple(1, 1, 1, 1)
    True
    >>> is_on_apple(1, 2, 3, 4)
    False
    >>> is_on_apple(0, 1, 0, 1)
    True
    >>> is_on_apple(0, 2, 0, 1)
    False
    >>> is_on_apple(2, 0, 1, 0)
    False
    '''
    return False # REPLACE FUNCTION BODY WITH YOUR CODE


def is_on_self(state):
    return len(set(state['snake'])) != len(state['snake'])


def new_apple(state):
    all_positions = set(
        itertools.product(range(state['width']), range(state['height'])))
    snake_positions = set(state['snake'])
    available_positions = all_positions - snake_positions
    state['apple'] = random.choice(list(available_positions))


def change_direction(current_direction, new_direction):
    ''' (String, String) -> String

    Returns the next direction the snake should be heading.
    If the new direction would turn the snake completely around,
    the old direction is maintained.

    >>> change_direction('left', 'right')
    'left'
    >>> change_direction('right', 'left')
    'right'
    >>> change_direction('up', 'left')
    'left'
    >>> change_direction('right', 'down')
    'down'
    >>> change_direction('up', 'down')
    'up'
    '''
    return current_direction # REPLACE FUNCTION BODY WITH YOUR CODE


def update(state, action):
    if action == 'restart':
        return initial_state(state['width'], state['height'])
    if state['alive']:
        if is_on_self(state):
            state['alive'] = False
            return state
        elif action == 'tick':
            return move(state, state['direction'])
        else:
            state['direction'] = change_direction(state['direction'], action)
            return state
    else:
        return state