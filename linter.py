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
        'rulesets:,': 'cleancode,codesize,controversial,design,naming,unusedcode'
    }

    def cmd(self):
        settings = self.get_view_settings()
        rulesets = settings.get('rulesets') or self.defaults['rulesets']

        if rulesets.endswith(".xml"):
            rulesets_file = self.resolve_rulesets_filename(rulesets)

            if rulesets_file is not None:
                return ('phpmd', '${temp_file}', 'text', rulesets_file)

            logger.error('file not found - %s' % rulesets)

        return ('phpmd', '${temp_file}', 'text', rulesets)

    def resolve_rulesets_filename(self, rulesets_file):
        if os.path.basename(rulesets_file) is not rulesets_file:
            if not os.path.isabs(rulesets_file):
                settings = self.get_view_settings()
                working_dir = self.get_working_dir(settings)
                if working_dir is None:
                    return None

                # Resolve path relative to current working dir
                rulesets_file = os.path.abspath(os.path.join(working_dir, rulesets_file))

            # Absolute file path
            if os.path.isfile(rulesets_file):
                return rulesets_file

            return None

        if not self.filename:
            # The file is not yet saved
            return None

        path = os.path.dirname(self.filename)

        # Traverse up the directory tree and try to find the file
        while True:
            file = os.path.join(path, rulesets_file)
            if os.path.isfile(file):
                return file

            newpath = os.path.dirname(path)
            if path == newpath:
                # We have reached the root directory
                return None

            path = newpath

        return None
