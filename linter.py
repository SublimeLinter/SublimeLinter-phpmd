from SublimeLinter.lint import Linter, WARNING


class Phpmd(Linter):
    cmd = ('phpmd', '${temp_file}', 'text')
    regex = (
        r'(?P<filename>.+):(?P<line>\d+)'
        r'\s*(?P<message>.+)$'
    )
    on_stderr = None  # handle stderr via regex
    default_type = WARNING
    tempfile_suffix = 'php'
    defaults = {
        'selector': 'source.php, text.html.basic',
        '@rulesets:,': 'cleancode,codesize,controversial,design,naming,unusedcode'
    }
