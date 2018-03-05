#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Dmitry Tsoy
# Copyright (c) 2013 Dmitry Tsoy
#
# License: MIT
#

"""This module exports the Phpmd plugin class."""

from SublimeLinter.lint import Linter, WARNING


class Phpmd(Linter):
    """Provides an interface to phpmd."""

    syntax = ('php', 'html', 'html 5')
    cmd = ('phpmd', '@', 'text')
    regex = (
        r'(?P<filename>.+):(?P<line>\d+)'
        r'\s*(?P<message>.+)$'
    )
    default_type = WARNING
    tempfile_suffix = 'php'
    defaults = {
        '@rulesets:,': 'cleancode,codesize,controversial,design,naming,unusedcode'
    }
