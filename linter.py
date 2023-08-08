from SublimeLinter.lint import Linter, TransientError, WARNING


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

    def cmd(self):
        if self.settings['lint_mode'] != 'background':
            # lint real files only, but only if the buffer is not dirty
            window = self.view.window()
            if window and self.view.is_dirty() or not self.view.file_name():
                window.status_message("phpmd: please save to lint this file")
                raise TransientError("Abort.  Buffer is dirty.")

            self.tempfile_suffix = '-'
            return ('phpmd', '${file_on_disk}', 'text')

        return ('phpmd', '${temp_file}', 'text')
