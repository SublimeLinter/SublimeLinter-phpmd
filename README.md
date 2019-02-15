SublimeLinter-phpmd
=========================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-phpmd.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-phpmd)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [phpmd](http://phpmd.org/documentation/index.html).
It will be used with files that have the "PHP", "HTML" and "HTML5" syntax.


## Installation

SublimeLinter must be installed in order to use this plugin. 

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before installing this plugin, ensure that `phpmd` is installed on your system.
To install `phpmd`, do the following:

1. Install [php](http://php.net).

2. Install [pear](http://pear.php.net).

3. Install `phpmd` by typing the following in a terminal:
   ```
   pear channel-discover pear.phpmd.org
   pear channel-discover pear.pdepend.org
   pear install --alldeps phpmd/PHP_PMD
   ```

### Alternative installation using [composer](https://getcomposer.org/):

1. Install [composer](https://getcomposer.org/).
2. Install `phpmd` using below command:
   ```
   composer global require phpmd/phpmd
   ```
3. Make sure composer global bin directory is available in $PATH
   ```
   export PATH=~/.composer/vendor/bin:$PATH
   ```

## Settings

You can specify a ruleset by setting `SublimeLinter.linters.phpmd.rulesets` in User settings or Project settings. The value can be a list of builtin rulesets, or path to a XML file with your custom rulesets. If the value is set to a filename, the first file found in the current directory or its parent directories is used. Default value is `cleancode,codesize,controversial,design,naming,unusedcode`.

- SublimeLinter settings: http://sublimelinter.com/en/latest/settings.html
- Linter settings: http://sublimelinter.com/en/latest/linter_settings.html
