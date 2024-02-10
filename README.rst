NAME

::

    OPD - original programmer daemon

SYNOPSIS

::

    opd <cmd> [key=val] 
    opd <cmd> [key==val]
    opd [-c] [-v] [-d]


DESCRIPTION

::

    OPD is a python3 library implementing the 'opd' package. It
    provides all the tools to program a bot, such as disk perisistence
    for configuration files, event handler to handle the client/server
    connection, code to introspect modules for commands, deferred
    exception handling to not crash on an error, a parser to parse
    commandline options and values, etc.

    OPD provides a demo bot, it can connect to IRC, fetch and
    display RSS feeds, take todo notes, keep a shopping list
    and log text. You can also copy/paste the service file and run
    it under systemd for 24/7 presence in a IRC channel.

    OPD is Public Domain.


INSTALL


::

    $ pipx install opd


USAGE

::

    without any argument the program does nothing

    $ opd
    $

    see list of commands

    $ od cmd
    cmd,err,mod,req,thr,ver

    list of modules

    $ opd mod
    cmd,err,fnd,irc,log,mod,req,rss,tdo,thr

    use mod=<name1,name2> to load additional
    modules

    $ opd cfg mod=irc

    start a console

    $ opd -c mod=irc,rss
    >

    use -v for verbose

    $ opd -cv mod=irc
    OPD started CV started Sat Dec 2 17:53:24 2023
    >

    start daemon

    $ opd -d
    $ 


CONFIGURATION


::

    irc

    $ opd cfg server=<server>
    $ opd cfg channel=<channel>
    $ opd cfg nick=<nick>

    sasl

    $ opd pwd <nsvnick> <nspass>
    $ opd cfg password=<frompwd>

    rss

    $ opd rss <url>
    $ opd dpl <url> <item1,item2>
    $ opd rem <url>
    $ opd nme <url< <name>


COMMANDS


::

    cmd - commands
    cfg - irc configuration
    dlt - remove a user
    dpl - sets display items
    fnd - find objects 
    log - log some text
    met - add a user
    mre - displays cached output
    pwd - sasl nickserv name/pass
    rem - removes a rss feed
    req - reconsider
    rss - add a feed
    thr - show the running threads


SYSTEMD


::

    save the following it in /etc/systemd/system/opd.service and
    replace "<user>" with the user running pipx


    [Unit]
    Description=original programmer daemon
    Requires=network.target
    After=network.target

    [Service]
    Type=simple
    User=<user>
    Group=<user>
    WorkingDirectory=/home/<user>/.opd
    ExecStart=/home/<user>/.local/pipx/venvs/lopd/bin/opd -d
    RemainAfterExit=yes

    [Install]
    WantedBy=multi-user.target


    then run this

    $ mkdir ~/.opd
    $ sudo systemctl enable opd --now

    default channel/server is #opd on localhost


FILES

::

    ~/.opd
    ~/.local/bin/opd
    ~/.local/pipx/venvs/opd/


AUTHOR


::

    Bart Thate <bthate@dds.nl>


COPYRIGHT


::

    OPD is Public Domain.
