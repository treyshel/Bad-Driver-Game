import curses, driver, time


def run(init, update, view, rate=None):
    '''(State, (String, State) -> State, (State, Int, Int) -> String, Int) -> None

    Helper inspired by The Elm Architecture for running simple terminal applications.
    `init` is the initial state of the application.
    `update` is a transition function from the current state
        to the next state when given an input character.
    `view` returns the string that should be printed for the current state of the application
        given the width and height of the curses window.
    `rate` is the number of times per second 'TICK` will be provided to update. By default,
        `rate` is none, and the application will block on input. If `rate` is provided,
        the application will not block on input.

    For example, a simple counter application might look like:

    def update(key, state):
        return state + 1
    
    def view(state, width, height):
        return 'The current number is: {}'.format(state)

    if __name__ == '__main__':
        run(0, update, view)
    '''

    def helper(stdscr):
        state = init
        y, x = stdscr.getmaxyx()
        stdscr.addstr(0, 0, view(state, x, y))
        if not (rate is None):
            stdscr.nodelay(1)
            wait = 1 / rate
            previous_tick = time.time()
        while True:
            if not (rate is None) and time.time() - previous_tick > wait:
                previous_tick = time.time()
                state = update('TICK', state)
                y, x = stdscr.getmaxyx()
                stdscr.addstr(0, 0, view(state, x, y))
            try:
                key = stdscr.getkey()
            except KeyboardInterrupt:
                return
            except:
                pass
            else:
                stdscr.clear()
                state = update(key, state)
                y, x = stdscr.getmaxyx()
                stdscr.addstr(0, 0, view(state, x, y))

    curses.wrapper(helper)


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
    state = state.game_update(key_to_action(key))
    if state.keep_going():
        return state
    else:
        print('GAME OVER')
        time.sleep(3)
        exit()


def view(state, width, height):
    return str(state)


def main():
    run(driver.Driver(50, 20, 25), update, view, 15)


if __name__ == '__main__':
    main()