#!/usr/bin/python3
import cmd
from models.base_model import BaseModel

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

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
        if not arg:
            print("** class name missing **")
        elif  arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            inst = BaselModel()
            inst.save()
            print(inst.id)

    def do_show(self, args):
        """Prints the string representation of an instance"""
        args = args.split()
        if not args:
            print("** class name missing **")
        elif arg1 == "BaselMode":
            print("** class doesn't exist **")
        elif arg2 is None:
            print("** instance id missing **")
        else:




if __name__ == '__main__':
    HBNBCommand().cmdloop()
