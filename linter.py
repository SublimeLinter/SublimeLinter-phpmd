import logging
import os
from SublimeLinter.lint import Linter, WARNING

logger = logging.getLogger('SublimeLinter.plugins.phpmd')

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
    }

    default_ruleset = 'cleancode,codesize,controversial,design,naming,unusedcode'

    def cmd(self):
        cmd = ('phpmd', '${temp_file}', 'text')

        settings = Linter.get_view_settings(self)
        rulesets = settings.get('rulesets')
        
        if rulesets.endswith(".xml"):
            rulesets_file = self.get_conf_file(rulesets)

            if rulesets_file:
                return ('phpmd', '${temp_file}', 'text', rulesets_file)

            logger.error('file not found - %s' % rulesets)
            rulesets = self.default_ruleset
            
        return ('phpmd', '${temp_file}', 'text', rulesets)

    def get_conf_file(self, filename):

        if os.path.isfile(filename) and os.path.basename(filename) is not filename:
            return filename

        if not self.filename:
            return False

        path = os.path.dirname(self.filename)

        while True:
            newpath = os.path.dirname(path)

            if path == newpath:
                return False

            file = os.path.join(path, filename)

            if os.path.isfile(file):
                return file

            path = newpath

        return False