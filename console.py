#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    """A interpreter for HBNB."""

    prompt = '(hbnb)'

    def do_quit(self, arg):
        """exit from program"""
        return True
    def do_EOF(self, arg):
        """end of file to leave program"""
        print()
        return True
    def emptyline(self):
        """empty line + ENTER shouldn’t execute anything"""
        pass
    def help_quit(self):
        """ information for the quit command."""
        print("Quit command to exit the program")
        print()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
