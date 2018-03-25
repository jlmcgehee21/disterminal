# -*- coding: utf-8 -*-

"""Console script for disterminal."""
import numpy as np
import sys
import click
from .plotting import plot
from . import messages
from . import helpers


@click.command(epilog=messages.EPILOG, help=messages.HELP_TEXT,
               context_settings=messages.CONTEXT_SETTINGS)
@click.argument('distribution')
@click.argument('function')
@click.argument('func_args', nargs=-1, type=float)
@click.option('--xlim', nargs=2, default=(None, None), type=float)
def main(distribution, function, func_args, xlim):

    dist = helpers.get_dist_callable(distribution)

    fun = helpers.get_fun_callable(dist, distribution, function)

    main_call = lambda x: fun(x, *func_args)

    xmin, xmax = xlim

    helpers.check_nan(main_call)

    if xmin is None or xmax is None:
        x = helpers.autorange(main_call, function)
    else:
        x = np.linspace(xmin, xmax, 100)

    y = main_call(x)

    plot(x, y, distribution, function)

    return 0



if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
