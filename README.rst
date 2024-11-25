**NAME**


``opd`` - Original Programmer Daemon


**SYNOPSIS**

|
| ``opdctl <cmd> [key=val] [key==val]``
| ``opd`` 
| ``opds``
|

**DESCRIPTION**


OPD contains all the python3 code to program objects in a functional
way. It provides a base Object class that has only dunder methods, all
methods are factored out into functions with the objects as the first
argument. It is called Object Programming (OP), OOP without the
oriented.

OPD allows for easy json save//load to/from disk of objects. It
provides an "clean namespace" Object class that only has dunder
methods, so the namespace is not cluttered with method names. This
makes storing and reading to/from json possible.

OPD has all you need to program a unix cli program, such as disk
perisistence for configuration files, event handler to handle the
client/server connection, deferred exception handling to not crash
on an error, etc.

OPD is Public Domain.

1. You need to set PYTHONPATH="." if you run this locally.
2. You might need to uninstall and rm -fR ~/.cache/pip in case of error.


**INSTALL**

installation is done with pipx

|
| ``$ pipx install opd``
| ``$ pipx ensurepath``
|
| <new terminal>
|
| ``$ opdctl srv > opd.service``
| ``$ sudo mv opd.service /etc/systemd/system/``
| ``$ sudo systemctl enable opd --now``
|
| joins ``#opd`` on localhost
|

**USAGE**

use ``opdctl`` to control the program, default it does nothing

|
| ``$ opdctl``
| ``$``
|

see list of commands

|
| ``$ opd cmd``
| ``cfg,cmd,dne,dpl,err,exp,imp,log,mod,mre,nme,``
| ``now,pwd,rem,req,res,rss,srv,syn,tdo,thr,upt``
|

start daemon

|
| ``$ opd``
| ``$``
|

start service

|
| ``$ opds``
| ``<runs until ctrl-c>``
|

show request to the prosecutor

|
| $ ``opd req``
| Information and Evidence Unit
| Office of the Prosecutor
| Post Office Box 19519
| 2500 CM The Hague
| The Netherlands
|

**COMMANDS**

here is a list of available commands

|
| ``cfg`` - irc configuration
| ``cmd`` - commands
| ``dpl`` - sets display items
| ``err`` - show errors
| ``exp`` - export opml (stdout)
| ``imp`` - import opml
| ``log`` - log text
| ``mre`` - display cached output
| ``now`` - show genocide stats
| ``pwd`` - sasl nickserv name/pass
| ``rem`` - removes a rss feed
| ``res`` - restore deleted feeds
| ``req`` - reconsider
| ``rss`` - add a feed
| ``syn`` - sync rss feeds
| ``tdo`` - add todo item
| ``thr`` - show running threads
| ``upt`` - show uptime
|

**CONFIGURATION**

irc

|
| ``$ opdctl cfg server=<server>``
| ``$ opdctl cfg channel=<channel>``
| ``$ opdctl cfg nick=<nick>``
|

sasl

|
| ``$ opdctl pwd <nsvnick> <nspass>``
| ``$ opdctl cfg password=<frompwd>``
|

rss

|
| ``$ opdctl rss <url>``
| ``$ opdctl dpl <url> <item1,item2>``
| ``$ opdctl rem <url>``
| ``$ opdctl nme <url> <name>``
|

opml

|
| ``$ opdctl exp``
| ``$ opdctl imp <filename>``
|

**SOURCE**

source is at `https://github.com/bthate/opd  <https://github.com/bthate/opd>`_


**FILES**

|
| ``~/.opd``
| ``~/.local/bin/opd``
| ``~/.local/bin/opdc`
| ``~/.local/bin/opdctl``
| ``~/.local/bin/opds``
| ``~/.local/pipx/venvs/opd/*``
|

**AUTHOR**

|
| Bart Thate <``bthate@dds.nl``>
|

**COPYRIGHT**

|
| ``OPD`` is Public Domain.
|