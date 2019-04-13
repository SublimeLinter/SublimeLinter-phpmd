from SublimeLinter.lint import Linter, WARNING


class Phpmd(Linter):
    cmd = ('phpmd', '${temp_file}', 'text')
    regex = (
        # For now, do *NOT* capture 'filename' since phpmd reports 'real'
        # paths, and Sublime and SL cannot map such paths to the original
        # `view.file_name()`.
        r'(.+):(?P<line>\d+)\s*(?P<message>.+)$'
    )
    on_stderr = None  # handle stderr via regex
    default_type = WARNING
    tempfile_suffix = 'php'
    defaults = {
        'selector': 'source.php, text.html.basic',
        '@rulesets:,': 'cleancode,codesize,controversial,design,naming,unusedcode'
    }
