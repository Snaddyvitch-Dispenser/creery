beem - Unofficial Python 3 Library for Steem
===============================================

!!!Alpha-State, be carefull!!!

steemi is an unofficial python 3 library for steem, which is created new from scratch from https://github.com/xeroc/python-bitshares.

.. image:: https://travis-ci.org/holgern/beem.svg?branch=master
    :target: https://travis-ci.org/holgern/beem

.. image:: https://ci.appveyor.com/api/projects/status/lnk5385dv0c2j28l?svg=true
    :target: https://ci.appveyor.com/project/holger80/beem

.. image:: https://circleci.com/gh/holgern/beem.svg?style=svg
    :target: https://circleci.com/gh/holgern/beem

.. image:: https://codecov.io/gh/holgern/beem/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/holgern/beem
  
.. image:: https://readthedocs.org/projects/beem/badge/?version=latest
  :target: http://beem.readthedocs.org/en/latest/?badge=latest

Installation
============
For Debian and Ubuntu, please ensure that the following packages are installed:
        
.. code:: bash

    sudo apt-get install build-essential libssl-dev python-dev

For Fedora and RHEL-derivatives, please ensure that the following packages are installed:

.. code:: bash

    sudo yum install gcc openssl-devel python-devel

For OSX, please do the following::

    brew install openssl
    export CFLAGS="-I$(brew --prefix openssl)/include $CFLAGS"
    export LDFLAGS="-L$(brew --prefix openssl)/lib $LDFLAGS"
    
Install beem by pip::

    pip install -U beem
    
You can install beem from this repository if you want the latest
but possibly non-compiling version::

    git clone https://github.com/holgern/beem.git
    cd beem
    python setup.py build
    
    python setup.py install --user

Run tests after install::

    pytest

Documentation
=============
Documentation is available at http://beem.readthedocs.io/en/latest/

Changelog
=========

0.19.3
------
* Add Comment/Post
* Add Witness
* Several bugfixes
* Added all transactions that are supported from steem-python
* New library name planned: beem

0.19.2
------
* Notify and websocket fixed
* Several fixes

0.19.1
------
* Imported from https://github.com/xeroc/python-bitshares 
* Replaced all BitShares by Steem
* Flake8 fixed
* Unit tests are working
* renamed to beem
* Docs fixed
* Signing fixed
* pysteem: Account, Amount, Asset, Block, Blockchain, Instance, Memo, Message, Notify, Price, Steem, Transactionbuilder, Vote, Witness are working


License
=======
This library is licensed under the MIT License.

Acknowledgements
================
https://github.com/xeroc/python-bitshares and https://github.com/xeroc/python-graphenelib were created by Fabian Schuh (xeroc).