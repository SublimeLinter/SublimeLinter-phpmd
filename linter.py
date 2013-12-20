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
    regex = (
        r'(?P<filename>.+):(?P<line>\d+)'
        r'(?P<message>.+)$'
    )
    executable = 'phpmd'
    tempfile_suffix = 'php'

    def cmd(self):
        """
        Return a string with the command line to execute.
        """
        command = ['phpmd', self.filename, 'text', 'cleancode,codesize,controversial,design,naming,unusedcode']

        return command
