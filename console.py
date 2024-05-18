#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage

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
            return
        try:
            new_instance = eval(args)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an instance"""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        class_name, id_number = args
        try:
            obj_dict = storage.all()
            key = f"{class_name}.{id_number}"
            if key in obj_dict:
                print(obj_dict[key])
            else:
                print("** no instance found **")
                return
        except NameError:
            print("** class doesn't exist **")
            return

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        class_name, id_number = args
        try:
            dest = storage.all()
            key = f"{class_name}.{id_number}"
            if key in dest:
                del dest[key]
                storage.save()
            else:
                print("** instance id missing **")
                return
        except NameError:
            print("** class doesn't exist **")
            return

    def do_all(self, args):
        """Prints all string representation of all instances based or not on the class name."""
        obj_dict = storage.all()
        if args:
            try:
                eval(args)
                fil_obj = [str(obj) for key, obj in obj_dict.items() if key.startswith(args)]
                print(fil_obj)
            except NameError:
                print("** class doesn't exist **")
        else:
            all_objs = [str(obj) for obj in obj_dict.values()]
            print(all_objs)

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return



if __name__ == '__main__':
    HBNBCommand().cmdloop()
