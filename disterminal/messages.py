from scipy import stats

VALID_DIST_TYPES = ['_discrete_distns', '_continuous_distns']

VALID_DIST_NAMES = ', '.join([x for x in dir(stats)
                    if any(y in str(type(getattr(stats, x)))
                           for y in VALID_DIST_TYPES)])
HELP_TEXT = 'Supported Distributions: ' + VALID_DIST_NAMES

EPILOG = 'See https://docs.scipy.org/doc/scipy/reference/stats.html for documentation of the scipy api.'

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
