import subprocess
from .terminalsize import get_terminal_size

def plot(x, y, distribution, function):
    term_x, term_y = get_terminal_size()

    gnuplot = subprocess.Popen(["gnuplot"],
                               stdin=subprocess.PIPE)

    _plot_command(gnuplot,
                  'set term dumb {} {}\n'.format(term_x, term_y - 2))
    _plot_command(gnuplot,
                  'set title \'{}.{}\'\n'.format(distribution, function))
    _plot_command(gnuplot, 'set border 3\n')
    _plot_command(gnuplot, 'set nokey\n')
    _plot_command(gnuplot, 'set tics out nomirror\n')
    _plot_command(gnuplot,
                  'plot \'-\' with impulses\n')

    for i,j in zip(x,y):
       _plot_command(gnuplot, '%f %f\n' % (i,j))

    _plot_command(gnuplot, 'e\n')
    gnuplot.stdin.flush()

def _plot_command(gnuplot, string):
    formatted = bytes(string, 'utf-8')
    gnuplot.stdin.write(formatted)
