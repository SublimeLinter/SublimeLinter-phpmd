from SublimeLinter.lint import Linter, WARNING


class Phpmd(Linter):
    regex = (
        r'(.+):(?P<line>\d+)\s*(?P<message>.+)$'
    )
    on_stderr = None  # handle stderr via regex
    default_type = WARNING
    tempfile_suffix = 'php'
    defaults = {
        'selector': 'embedding.php, source.php',
        '@rulesets:,': 'cleancode,codesize,controversial,design,naming,unusedcode'
    }

    @classmethod
    def should_lint(cls, view, settings, reason):
        # type: (sublime.View, LinterSettings, Reason) -> bool
        """Decide whether the linter can run at this point in time."""
        if settings['real_file_mode'] and (
            view.is_dirty() or not view.file_name()
        ):
            return False

        return super().should_lint(cls, view, settings, reason)

    def cmd(self):
        target = '$file_on_disk' if self.settings['real_file_mode'] else '$temp_file'
        self.tempfile_suffix = '-' if self.settings['real_file_mode'] else 'php'
        return ('phpmd', target, 'text')
