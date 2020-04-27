# PyBearBull
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blueviolet)](https://www.gnu.org/licenses/agpl-3.0)
![Build and Test](https://github.com/bl1nk1n/pybearbull/workflows/Build%20and%20Test/badge.svg?event=release)

A pure python implementation of the ManBearBull project.

## ManBearBull Project
The aim of the ManBearBull project is to provide implementations of common
tools and functionalities useful to financial instrument trading.  This includes
technical analysis tools, trade history tools, and trading tools.

## Table of Contents
* [Functionality](#functionality)
    * [Technical Analysis Tools](#technical-analysis-tools)
    * [Trade History Tools](#trade-history-tools)
    * [Trading Tools](#trading-tools)
* [Building](#building)
    * [Cloning PyBearBull From Git](#cloning-pybearbull-from-git)
    * [Virtual Environment](#virtual-environment)
    * [Dependencies](#dependencies)
* [Running](#running)
* [Testing](#testing)
* [Contributing](#contributing)
* [Libraries](#libraries)
* [TODO](docs/TODO)
* [CHANGELOG](docs/CHANGELOG)

## Functionality

### Technical Analysis Tools
Currently there are no tools that are written to completion.

### Trade History Tools
Currently this functionality does not exist.

### Trading Tools
Currently this functionality does not exist.


## Building

### Cloning PyBearBull From Git
To clone this project via SSH, use one of the following:
* `git clone git@github.com:bl1nk1n/pybearbull.git`
* `git clone git@bitbucket.org:SamuelHentschel/pybearbull.git`
* `git clone git@gitlab.com:bl1nk1n/pybearbull.git`

To clone this project via HTTPS, use one of the following:
* `git clone https://github.com/bl1nk1n/pybearbull.git`
* `git clone https://bl1nk1n@bitbucket.org/SamuelHentschel/pybearbull.git`
* `git clone https://gitlab.com/bl1nk1n/pybearbull.git`

### Virtual Environment
To make sure you do not install any packages that might conflict with your
system's packages, it is recommended to set up a virtual environment.  To
do this, download a copy of `virtualenv` or a similar program from your
package manager.  We will assume you are using `virtualenv` on linux for
the rest of this section.  

With `virtualenv` installed, run the following command inside the PyBearBull 
top-level directory to create a new virtual environment: 
`$ virtualenv -p python3 pybearbull_venv`.  You can name the virtual environment
whatever you want, but for clarity we named it `pybearbull_venv`.  To activate 
the environment before proceeding, issue the following: 
`$ source pybearbull_env/bin/activate`.  This activates the virtual environment 
for this project.  

While in this environment, any python packages you install will be kept in
`pybearbull_venv` which is separate from your system python packages.  If you
leave the environment and come back, they will still be installed as before.

To deactivate this environment (when done working with the project) issue the
following: `$ deactivate`.  You should now be using your system's python
packages again.

### Dependencies
Currently there are no dependencies.

## Running
Currently there is no way to run this project.

## Testing
To run the tests, you need to install the following packages in addition to the
normal [dependencies](#dependencies):
* pytest
* pytest-cov
* pytest-flakes
<!--* pytest-xdist-->
It is recommended to use a [virtual environment](#virtual-enviornment) to avoid
issues regarding conflicting packages.  After installing the dependencies
(hopfully in a virtual environment), issue the following command inside the
pybearbull top-level directory to run the tests, code coverage checker and
linter: `$ python -m pytest --flakes --cov=pybearbull/ tests/`.


## Contributing
Please feel free to contribute.  Take a look at the documentation to see the
branching, repository, and versioning structure first.  Fork the project from
the appropriate branch (at first it will be the master branch until a release is
made).  Make sure to not only write code but comment it, document it, unit test,
and integration test it.  Testing is done via Github, Gitlab and Bitbucket (to a
lesser extent); you do not need to write for all three although it would be
preferred as it needs to be done sooner or later.


## Libraries
Currently none of the parts of this project have been split off into libraries.
