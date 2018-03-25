#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from click.testing import CliRunner
from disterminal import cli

@pytest.fixture
def runner():
    return CliRunner()

def test_cli_no_args(runner):
    """Test the CLI."""
    result = runner.invoke(cli.main)
    assert result.exit_code == 2

def test_cli_help(runner):
    for help_opt in ['-h', '--help']:
        help_result = runner.invoke(cli.main, [help_opt])
        assert help_result.exit_code == 0
        assert 'Supported Distributions:' in help_result.output
        assert 'norm, pareto' in help_result.output
        assert 'https://docs.scipy.org/doc/scipy/reference/stats.html' in help_result.output

def test_bad_distribution(runner):
    result = runner.invoke(cli.main, ['foo', 'bar'])
    assert 'scipy.stats does not contain distribution "foo"\n' == result.output

def test_bad_function(runner):
    result = runner.invoke(cli.main, ['norm', 'bar'])
    assert 'scipy.stats.norm does not have function "bar"\n' == result.output

def test_all_nan(runner):
    result = runner.invoke(cli.main, ['beta', 'pdf', '0', '0'])
    assert 'all values are NaN, nothing to plot...\n' == result.output
