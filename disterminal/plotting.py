import subprocess
import pty
import os
import sys
from fabulous.color import fg256, bg256
from .terminalsize import get_terminal_size


def plot(x, y, distribution, function, color):
    term_x, term_y = get_terminal_size()

    s = script(distribution, function)

    for i, j in zip(x, y):
        s += '%f %f\n' % (i, j)

    master, slave = pty.openpty()
    gnuplot = subprocess.Popen(
        ["gnuplot", "-p"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    output = gnuplot.communicate(bytes(s, 'utf-8'))[0]

    plot_color = bytes(str(fg256(color, '*')), 'utf-8')
    with_color = output.replace(
        b'*',
        plot_color,
    )

    sys.stdout.buffer.write(with_color)


def script(distribution, function):
    term_x, term_y = get_terminal_size()

    return 'set term dumb size {} {}\n'.format(term_x, term_y - 2) +\
        'set title \'{}.{}\'\n'.format(distribution, function) +\
        'set border 3\n' +\
        'set nokey\n' +\
        'set tics out nomirror\n' +\
        'plot \'-\' with impulses\n'
