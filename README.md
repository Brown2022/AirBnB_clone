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
