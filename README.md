SublimeLinter-phpmd
=========================

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter3) provides an interface to [phpmd](http://phpmd.org/documentation/index.html). It will be used with files that have the “php”, “html” and “html5” syntax.

## Installation

### Linter installation
Before installing this plugin, you must ensure that `phpmd` is installed on your system. To install `phpmd`, do the following:

1. Install [php](http://php.net).

2. Install [pear](http://pear.php.net).

3. Install `phpmd` by typing the following in a terminal:
   ```
   pear channel-discover pear.phpmd.org
   pear channel-discover pear.pdepend.org
   pear install --alldeps phpmd/PHP_PMD
   ```

Now you can proceed to install the SublimeLinter-phpmd plugin.

### Plugin installation
Please use [Package Control](https://sublime.wbond.net/installation) to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette](http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html) and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `phpmd`. Among the entries you should see `SublimeLinter-phpmd`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings

Add php path to `paths`. Go to `Preferences: SublimeLinter Settings - User` and add the following.
```json
{
    "user": {
        "paths": {
            "linux": [],
            "osx": [
                "/usr/local/php5/bin/"
            ],
            "windows": []
        }
    }
}
```
For general information on how SublimeLinter works with settings, please see [Settings](http://sublimelinter.readthedocs.org/en/latest/settings.html). For information on generic linter settings, please see [Linter Settings](http://sublimelinter.readthedocs.org/en/latest/linter_settings.html).

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.

Thank you for helping out!
