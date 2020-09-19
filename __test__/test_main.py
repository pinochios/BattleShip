from threading import Thread
from msvcrt import getch
import click


class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass


"""a = 10

while True:
    try:
        x = int(input())
        if x < a:
            pass
        else:
            raise ValueTooLargeError
    except ValueError:
        print("Invalid value, please try again")
    except ValueTooLargeError:
        print("Too large value, please try again")
    else:
        break
"""

# up : '\x00H' down: '\x00P' left: '\x00K' Right: '\x00M'
click.echo('Continue? [yn] ', nl=False)
c = click.getchar()
click.echo()
if c == '\x00H':
    click.echo('Up')
elif c == '\x00P':
    click.echo('Down')
elif c == '\x00K':
    click.echo('Left')
elif c == '\x00M':
    click.echo('Down')
else:
    click.echo('Invalid input :(')


"""def KeyCheck():
    global Break_KeyCheck
    Break_KeyCheck = False

    while Break_KeyCheck:
        base = getch()
        if base == '\xe0':
            sub = getch()

            if sub == 'H':
                key = 'UP_KEY'
            elif sub == 'M':
                key = 'RIGHT_KEY'
            elif sub == 'P':
                key = 'DOWN_KEY'
            elif sub == 'K':
                key = 'LEFT_KEY'


Thread(target=KeyCheck).start()
# BACKGROUND CODE"""
