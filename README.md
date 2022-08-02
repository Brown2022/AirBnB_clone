# AirBnB_clone

Description 0f the prject
-------------------------

The Console: This is where we created our objects for this projects, and we also learn and implement file serialization and also created our first engine called the file storage.

The HTML: This is where we learn to make things pretty, beautiful and give isual interface for future users.

MySQL: This is where we learn different types of storage and also new type of database where we will be able to find a unique way that we can best store objects.This is a database management system that deals with the structured collection of data.

Deployment of HTML with Fabrics
-------------------------------
This is where we took all we have made and put them in our server.

Flask Web Application Server
----------------------------
This is where we took the module in storage and integrate them with our HTML

REST API
--------
This is where we took things that are in object form and put them in json.

WEB Dynamic
-----------
This where we took the json API and integrate it with the HTML so we will be able to share our WEB Application with other people.

Description of the command interpreter
--------------------------------------
A command interpreter is the part of a computer operating system that understands and executes commands that are entered interactively by a human being or from a program. In some operating systems, the command interpreter is called the shell.
Shell is a UNIX term for the interactive user interface with an operating system.

* how to start it 

* how to use it

Using the shell in interactive mode

The shell is running in such a way that it displays a prompt and a cursor (the little, blinking line) and is waiting for you to enter a command for it to execute. You execute commands in interactive mode by typing them in, followed by a press of the Enter key. The shell then translates your command to something the operating system understands and passes off control to the operating system so that it can actually carry out the task you have sent it. You'll notice that your cursor will disappear momentarily while the command is being carried out, and you cannot type anymore (at this point, the Bourne Shell program is no longer in control of your terminal -- the other program that you started by executing your command is). At some point the operating system will be finished working on your command and the shell will bring up a new prompt and the cursor as well and will then start waiting again for you to enter another command. 

Non-interactive shell:

As the name implies, a non-interactive shell is a type of shell that doesn’t interact with the user. We can run it through a script or similar. Also, it can be run through some automated process. In this case  .bashrc and .profile files do not get executed. The non-interactive shell influences the PATH variable. It is highly recommended to use the full path for a command in non-interactive shells. Non-interactive scripts can smoothly run in the background easily. This shell is generally a non-login shell because the calling user has logged in already. A shell that runs a script is always considered a non-interactive shell.

Scripts like Init and startup are considered non-interactive since they must run without human intervention.

How to check which type of shell is being used?

The type of shell being used can be detected (BASH only).
We can also determine if we are using an interactive or non-interactive shell by,

[[ $- == *i* ]] && echo ‘Interactive’ || echo ‘not-interactive’

* examples

KornShell (ksh): written by David Korn based on the Bourne shell sources[8] while working at Bell Labs

Public domain Korn shell (pdksh)

Bourne-Again shell (bash): written as part of the GNU Project to provide a superset of Bourne Shell functionality. This shell can be found installed and is the default interactive shell for users on most Linux systems.

Debian Almquist shell (dash): a modern replacement for ash in Debian and Ubuntu

Almquist shell (ash):
written as a BSD-licensed replacement for the Bourne Shell; often used in resource-constrained environments. The sh of FreeBSD, NetBSD (and their derivatives) are based on ash that has been enhanced to be POSIX conformant.

KornShell (ksh) is a Unix shell which was developed by David Korn at Bell Labs in the early 1980s and announced at USENIX on July 14, 1983.[1][2] The initial development was based on Bourne shell source code.[7] Other early contributors were Bell Labs developers Mike Veach and Pat Sullivan, who wrote the Emacs and vi-style line editing modes' code, respectively.[8] KornShell is backward-compatible with the Bourne shell and includes many features of the C shell, inspired by the requests of Bell Labs users.

The C shell (csh or the improved version, tcsh) is a Unix shell created by Bill Joy while he was a graduate student at University of California, Berkeley in the late 1970s. It has been widely distributed, beginning with the 2BSD release of the Berkeley Software Distribution (BSD) which Joy first distributed in 1978.[2][3] Other early contributors to the ideas or the code were Michael Ubell, Eric Allman, Mike O'Brien and Jim Kulp.[4]

The C shell is a command processor which is typically run in a text window, allowing the user to type and execute commands. The C shell can also read commands from a file, called a script. Like all Unix shells, it supports filename wildcarding, piping, here documents, command substitution, variables and control structures for condition-testing and iteration. What differentiated the C shell from others, especially in the 1980s, were its interactive features and overall style. Its new features made it easier and faster to use. The overall style of the language looked more like C and was seen as more readable.

On many systems, such as macOS and Red Hat Linux, csh is actually tcsh, an improved version of csh. Often one of the two files is either a hard link or a symbolic link to the other, so that either name refers to the same improved version of the C shell.
