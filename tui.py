import driver, time
from pybcca.tui_helper import run


def key_to_action(key):
    '''String -> String

    Translates `key` into the appropriate action string for the driver game.
    The examples outline the mapping between keys and actions.

    >>> key_to_action('KEY_LEFT')
    'left'
    >>> key_to_action('KEY_RIGHT')
    'right'
    >>> key_to_action('R')
    'restart'
    >>> key_to_action('r')
    'restart'
    >>> key_to_action('TICK')
    'tick'
    >>> key_to_action('anything else')
    '''
    if key == 'KEY_LEFT':
        return 'left'
    elif key == 'KEY_RIGHT':
        return 'right'
    elif key == 'KEY_UP':
        return 'up'
    elif key == 'KEY_DOWN':
        return 'down'
    elif key == 'r' or key == 'R':
        return 'restart'
    elif key == 'TICK':
        return 'tick'
    else:
        return None


def update(key, state):
    return state.game_update(key_to_action(key))


def final_view(state, w, h):
    return '''Game Over:
Score: {}
'''.format(state.score)


def view(state, width, height):
    return str(state)


def main():
    run(driver.Driver(50, 20, 25),
        update,
        view,
        15,
        quit_when=lambda s: not s.keep_going(),
        final_view=final_view)


if __name__ == '__main__':
    main()