import click
import numpy as np
import sys
from scipy import stats

AUTO_XLIMITS = {'cdf': (0, 10000, .05),
                'pdf': (-10000, 10000, .05),
                'ppf': (0, 1, .01)}

def get_dist_callable(distribution):
    try:
        return getattr(stats, distribution)
    except AttributeError:
        click.echo('scipy.stats does not contain distribution "{}"'.format(distribution))
        sys.exit(1)

def get_fun_callable(dist, distname, function):
    try:
        return getattr(dist, function)
    except AttributeError:
        click.echo('scipy.stats.{} does not have function "{}"'.format(distname, function))
        sys.exit(1)

def check_nan(main_call):
    x = np.arange(-100, 100, 1)
    y = main_call(x)

    if np.all(np.isnan(y)):
        click.echo('all values are NaN, nothing to plot...')
        sys.exit(1)

def autorange(main_call, function):
    limits = AUTO_XLIMITS.get(function, (-10000, 10000, .05))

    x = np.arange(*limits)
    y = main_call(x)

    min_y = 0.0001
    max_y = 0.9999
    x = x[np.logical_and(y >= min_y, y < max_y)]

    return np.linspace(x.min(), x.max(), 100)
