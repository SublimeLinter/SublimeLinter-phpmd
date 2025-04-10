SublimeLinter-phpmd
=========================

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [phpmd](http://phpmd.org/documentation/index.html).
It will be used with files that have the "PHP", "HTML" and "HTML5" syntax.


## Installation

### Install `SublimeLinter` and `SublimeLinter-phpmd`

Make sure [Package Control](https://packagecontrol.io) is installed.

1. Open the command palette (Ctrl + Shift + P)
2. Type **Package Control: Install Package** and select it.
3. Type **SublimeLinter** and select it.
4. Repeat steps 1-3 typing **SublimeLinter-phpmd** in step 3.

### Install `phpmd`

Choose one of the installation methods below.

A local install allows you to fine-tune `phpmd` on a per-project basis. A global install is available system-wide.

#### Local install with [Composer](https://getcomposer.org/)

On a command line inside your project:
```bash
composer require phpmd/phpmd
```

#### Global install with [Composer](https://getcomposer.org/)

```bash
composer global require phpmd/phpmd
```

Make sure the composer global bin directory is available in $PATH:

```bash
export PATH=~/.composer/vendor/bin:$PATH
```

#### Global install with [PEAR](https://pear.php.net)

```bash
pear channel-discover pear.phpmd.org
pear channel-discover pear.pdepend.org
pear install --alldeps phpmd/PHP_PMD
```

## Settings

- SublimeLinter settings: http://sublimelinter.com/en/latest/settings.html
- Linter settings: http://sublimelinter.com/en/latest/linter_settings.html

### Additional settings

If you want to use a baseline file, the linter needs to run on the actual files instead of the temporary files we need for real-time "background" linting. 
Therefore, set the "real_file_mode" setting to true.

```json
"linters": {
  "phpmd": {
    "real_file_mode": true
  }
}
```

### Rulesets

You can configure rules via the `rulesets` setting. This can be a list of rules, or a path to a custom ruleset file.

```json
  "linters": {
    "phpmd": {
      "rulesets": "codesize,unusedcode,naming"
    }
  }
```

```json
  "linters": {
    "phpmd": {
      "rulesets": "${folder}/phpmd.xml"
    }
  }
```
