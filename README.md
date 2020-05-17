SublimeLinter-phpmd
=========================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-phpmd.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-phpmd)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [phpmd](http://phpmd.org/documentation/index.html).
It will be used with files that have the "PHP", "HTML" and "HTML5" syntax.


## Installation

### Install `SublimeLinter` and `SublimeLinter-phpmd`

Make sure [Package Control](https://packagecontrol.io) is installed.

Open the command palette (Ctrl + Shift + P) and choose **Package Control: Install Package**. Type **SublimeLinter** and select it. Repeat this for **SublimeLinter-phpmd**.

### Install phpmd

#### phpmd local install (within a project) with [Composer](https://getcomposer.org/)

```bash
composer require phpmd/phpmd
```

Inside Sublime, go to **Preferences -> Package Settings -> SublimeLinter -> Settings**.

Set the `phpmd` executable by adding/editing:
```json
  "linters": {
    "phpmd": {
      "executable": "${folder}/vendor/bin/phpmd"
    }
  }
```

##### phpmd global install with [Composer](https://getcomposer.org/)

```bash
composer global require phpmd/phpmd
```

Make sure the composer global bin directory is available in $PATH:

```bash
export PATH=~/.composer/vendor/bin:$PATH
```

#### phpmd global install with [PEAR](https://pear.php.net)

```bash
pear channel-discover pear.phpmd.org
pear channel-discover pear.pdepend.org
pear install --alldeps phpmd/PHP_PMD
```

## Settings

- SublimeLinter settings: http://sublimelinter.com/en/latest/settings.html
- Linter settings: http://sublimelinter.com/en/latest/linter_settings.html


