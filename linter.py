from SublimeLinter.lint import Linter, WARNING


class Phpmd(Linter):
    cmd = ('phpmd', '${file}', 'text')
    regex = (
        r'(?P<filename>.+):(?P<line>\d+)'
        r'\s*(?P<message>.+)$'
    )
    default_type = WARNING
    tempfile_suffix = 'php'
    defaults = {
        'selector': 'source.php, text.html.basic',
        '@rulesets:,': 'cleancode,codesize,controversial,design,naming,unusedcode'
    }
