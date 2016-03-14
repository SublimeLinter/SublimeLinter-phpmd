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

from SublimeLinter.lint import highlight, Linter


class Phpmd(Linter):
    """Provides an interface to phpmd."""

    syntax = ('php', 'html', 'html 5')
    cmd = 'phpmd @ text'
    executable = 'phpmd'
    regex = (
        r'(?P<filename>.+):(?P<line>\d+)'
        r'\s*(?P<message>.+)$'
    )
    default_type = highlight.WARNING
    tempfile_suffix = 'php'
    defaults = {
        '@rulesets:,': 'cleancode,codesize,controversial,design,naming,unusedcode'
    }
    inline_overrides = 'rulesets'
    comment_re = r'\s*<!--'

    def cmd(self):
        """Create the cmd."""
        settings = Linter.get_view_settings(self)

        # attempt to get the command from settings if it is present
        if 'cmd' in settings:
            command = [settings.get('cmd')]
        else:
            command = [self.executable_path]

        command.append('@')
        command.append('text')

        return command
