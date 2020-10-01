[![Documentation Status](https://readthedocs.org/projects/lpn-doc-sphinx-primer-devel/badge/?version=latest)](https://lpn-doc-sphinx-primer-devel.readthedocs.io/)
[![Build Status](https://travis-ci.org/rexut/lpn-doc-sphinx-primer.svg?branch=master)](https://travis-ci.org/rexut/lpn-doc-sphinx-primer)

# Li-Pro.Net Sphinx Primer

This is about how to write Li-Pro.Net documentation with
[Sphinx](https://www.sphinx-doc.org).

## Howto build the documentation

The documentation is written using Sphinx documentation system. To
install it in a Python 3.x virtual environment, please do:

**Python 3.8 virtual environment:**

```bash
$: python3.8 -m venv --copies --promp="$(basename $(pwd))[$(python3.8 --version)]" .py38env
$: source .py38env/bin/activate
$: pip install --upgrade pip
$: pip install --upgrade setuptools
$: pip install --upgrade --requirement tools/requirements.txt
```

**Get help:**

```bash
$: make help
```

**Documentation tests:**

```bash
$: make doctest
$: make coverage
$: make linkcheck
$: make spelling
```

**Documentation builds:**

```bash
$: make html
$: make latexpdf
```

**Clean-up:**

```bash
$: make clean
$: deactivate
$: rm -rf .py38env
```

### System packages on Ubuntu (>= 16.04):

```bash
$: sudo apt-get install build-essential python3.8-dev
$: sudo apt-get install curl tar bzip2 woff2 eot-utils
$: sudo apt-get install fontconfig fontforge-nox
$: sudo apt-get install libfreetype6-dev librsvg2-bin icoutils
$: sudo apt-get install poppler-utils imagemagick pdf2svg
$: sudo apt-get install latexmk xindy unifont fonts-dejavu
$: sudo apt-get install fonts-wqy-microhei fonts-font-awesome
$: sudo apt-get install texlive-xetex texlive-pictures texlive-science
$: sudo apt-get install texlive-fonts-recommended texlive-fonts-extra
$: sudo apt-get install texlive-lang-european texlive-lang-english
$: sudo apt-get install enchant aspell aspell-en aspell-de
$: sudo apt-get install wamerican-huge wngerman wgerman-medical
```

### Sphinx bootstrap

For the purpose of later comprehension, the steps for setting up this
document with the help of `sphinx-quickstart` were recorded here:

```bash
$: sphinx-quickstart					\
       --sep --dot _                                    \
       --project "Li-Pro.Net Sphinx Primer"             \
       --author  "The LP/N Documentation Team"          \
       -v 0.0 --release 0.0.1                           \
       --language "en"                                  \
       --suffix ".rst"                                  \
       --master "index"                                 \
       --extensions "sphinx.ext.autosectionlabel"       \
       --ext-doctest                                    \
       --ext-coverage                                   \
       --ext-todo                                       \
       --ext-ifconfig                                   \
       --ext-intersphinx                                \
       --extensions "sphinx.ext.extlinks"               \
       --ext-mathjax                                    \
       --makefile                                       \
       --batchfile                                      \
       .
```
