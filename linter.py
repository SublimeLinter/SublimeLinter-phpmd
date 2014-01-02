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

from SublimeLinter.lint import Linter


class Phpmd(Linter):

    """Provides an interface to phpmd."""

    syntax = ('php', 'html', 'html 5')
    cmd = 'phpmd @ text'
    executable = 'phpmd'
    regex = (
        r'(?P<filename>.+):(?P<line>\d+)'
        r'(?P<message>.+)$'
    )
    defaults = {
        '@rulesets:,': 'cleancode,codesize,controversial,design,naming,unusedcode'
    }
    tempfile_suffix = 'php'
