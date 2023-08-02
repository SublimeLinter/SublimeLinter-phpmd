from SublimeLinter.lint import Linter, WARNING


class Phpmd(Linter):
    cmd = ('phpmd', '${file}', 'text')
    regex = (
        r'(.+):(?P<line>\d+)\s*(?P<message>.+)$'
    )
    on_stderr = None  # handle stderr via regex
    default_type = WARNING
    tempfile_suffix = '-'
    defaults = {
        'selector': 'embedding.php, source.php',
        '@rulesets:,': 'cleancode,codesize,controversial,design,naming,unusedcode'
    }
