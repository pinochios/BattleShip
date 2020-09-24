from elements import *
import click

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
    click.echo('Invalid input :(')"""


def keyboardInput():
    click.echo('wasd - move, qe - rotate, c - confirm', nl=False)
    c = click.getchar()
    click.echo()
    if c == 'w':
        key = 'up'
    elif c == 's':
        key = 'down'
    elif c == 'a':
        key = 'left'
    elif c == 'd':
        key = 'right'
    elif c == 'q':
        key = 'ccv'
    elif c == 'e':
        key = 'cv'
    elif c == 'c':
        key = 'confirm'
    else:
        return 'Invalid Input'
    return key
