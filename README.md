SublimeLinter-phpmd
=========================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-phpmd.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-phpmd)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [phpmd](http://phpmd.org/documentation/index.html).
It will be used with files that have the "PHP", "HTML" and "HTML5" syntax.


## Installation

First, install phpmd with Composer or PEAR.
Then install SublimeLinter and SublimeLinter-phpmd with Package Control.

### 1. Installing phpmd

Make sure [PHP](https://www.php.net) is installed.

#### 1.1 Installing phpmd with [Composer](https://getcomposer.org/):

##### 1.1.1 Local install (within a project)

1. Install `phpmd` from a command line:
```
composer require phpmd/phpmd
```
2. Open **Preferences -> Package Settings -> SublimeLinter -> Settings**
3. Set the `phpmd` executable by adding/editing:
```
  "linters": {
    "phpmd": {
      "executable": "${folder}/vendor/bin/phpmd"
    }
  }
```

##### 1.1.2 Global install

1. Install `phpmd` from a command line:
```
composer global require phpmd/phpmd
```
2. Make sure the composer global bin directory is available in $PATH
```
export PATH=~/.composer/vendor/bin:$PATH
```

#### 1.2 Installing phpmd with [PEAR](https://pear.php.net)

Install `phpmd` from a command line:
```
pear channel-discover pear.phpmd.org
pear channel-discover pear.pdepend.org
pear install --alldeps phpmd/PHP_PMD
```

### 2. Installing SublimeLinter

Make sure [Package Control](https://packagecontrol.io) is installed.

1. Open the command palette (Ctrl + Shift + P) and choose **Package Control: Install Package**.
2. Type **SublimeLinter** and select it.

### 3. Installing SublimeLinter-phpmd

1. Open the command palette (Ctrl + Shift + P) and choose **Package Control: Install Package**.
2. Type **SublimeLinter-phpmd** and select it.

## Settings

- SublimeLinter settings: http://sublimelinter.com/en/latest/settings.html
- Linter settings: http://sublimelinter.com/en/latest/linter_settings.html


