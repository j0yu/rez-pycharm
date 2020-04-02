# PyCharm Community Edition

[![CI](../..//workflows/CI/badge.svg?branch=master)](../../actions?query=workflow%3ACI+branch%3Amaster)

[rez] package to install stable releases of [pycharm].

Here are some beginners instructions on how to use this repository.

## Installation

1. Install [rez] via `python install.py` method
1. Clone/download this repository
1. Ensure at least the folder printed by
   this command `rez config local_packages_path`
1. Open terminal in (extracted) repository folder,
   run `rez build --install`

Visual Studio Code should now be installed as a [rez]
package named `pycharm_ce`.

## Usage

To run [pycharm]: `rez env pycharm_ce -- pycharm`

## Maintenance

Whenever new official release come out, update the `__version__`
in `package.py` then re-run `rez build --install`.

If you decide to make a better install or new `commands()` environment
setup, you can instead just update the `+local.` version number to indicate
new releases/versions of your own similar to, 
[PEP 540 local version segments]

[rez]: https://github.com/nerdvegas/rez
[pycharm]: https://blog.jetbrains.com/pycharm/category/announcement/
[PEP 540 local version segments]: https://www.python.org/dev/peps/pep-0440/#local-version-segments
