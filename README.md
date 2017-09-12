# Helicopter Escape
This application stimulates a helicopter trying to get out of some mountains and escape.

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

```python
def main():
```
- This function is used to run the application, and to draw out the gridth with the width, height, and the road width.
- It also helps check whether or not the helicopter has crashed.