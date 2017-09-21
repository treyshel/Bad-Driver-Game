# Before Using
install:
pip3 install --user pybcca


# Helicopter Escape
This application stimulates a helicopter trying to get out of some mountains and escape.
The goal is to try to escape and not crash.
- The higher a user goal, the more points he or she gets.

# Driver

The driver.py file acts like a core where all the functions are at, and everything is created in there.  Then all of the functions will later help in the tui.py which for this project is like the shell.

- score: an interger that starts at 0
- level: an interger that starts at 1
- left and right: Is the sides which causes the user to loose if it is touched.
- roadwidth:  The space left where the helicopter can fly in
- grid: Where the helicopter and the out of bounds will be



# tui

The tui.py file is used as the shell and uses all the functions from the driver.py.

- the user is always displayed the level and the score

```python
def key_to_action(key):
```
- Each key in this functions is used to move the helicopter up or down and left or right.
- Right arrow:  Moves the helicopter one space over to the right
- Left arrow:  Moves the helicopter one space over to the left
- Downn arrow:  Moves the helicopter one space down
- Up arrow:  Moves the helicopter one space up
- Space bar:  Makes the helicopter move faster and the points also increase faster
- R or r:  Starts the game over again during the game or after the user looses

```python
def main():
```
- This function is used to run the application, and to draw out the gridth with the width, height, and the road width.
- It also helps check whether or not the helicopter has crashed.

# Heli.txt

Text file that contains an ascii helicopter
- Displays the asii to the user once they win.

