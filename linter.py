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

    def cmd(self):
        if self.settings['lint_mode'] != 'background':
            self.tempfile_suffix = '-'
            return ('phpmd', '${file_on_disk}', 'text')

        return ('phpmd', '${temp_file}', 'text')
