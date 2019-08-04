# Black Hat Python Notes
Notes from the book Black Hat Python by Justin Seitz and my own experience

## The Network Basics
* Programmers have a number of third-party tools to create networked servers and clients in Python, but the core module
for all those tools is *socket*. This module exposes all of the necessary pieces to quickly write TCP and UDP clients
and servers, use raw sockets, and so forth. For the purposes of breaking in or maintaining access to target machines,
this module is all you really need. 

## Replacing Netcat
* Netcat is the utility knife of networking, so its no surprise that shrewd system administrators remove it from their
systems. Sometimes, servers do not have netcat installed but do have Python. In these cases, it is useful to create a
simple network client and server that you can use to push files, or to have a listener that gives you command-line access.
* If you've broken in through a web application, it is definitely worth dropping a Python callback to give you secondary
access without having to burn one of your trojans or backdoors.

## Building a TCP Proxy
There are a number of reasons to have a TCP proxy in your tool belt, both for forwarding traffic to bounce from host to
host, but also when accessing network-based software. When performing penetration tests in enterprise environments, you'll
commonly be faced with the fact that you can't run Wireshark, that you can't load 
