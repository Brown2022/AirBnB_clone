#!/usr/bin/python3
"""
The Console
"""


import cmd

class HBNBCommand(cmd.Cmd):
    """
    An interactive Command Line Interface
    """

    prompt = '(hbnb) '

    def do_emptyline(self):
        """
        Do nothing when empty line + enter
        """
        return False

    def do_EOF(self, arg):
        """
        Exit the Command Line
        """
        return True

    def do_quit(self, arg):
        """
        Exit the Command Line
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
