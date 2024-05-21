#!/usr/bin/python3
""" entry point of the command interprete"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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

    def do_create(self, args):
        """Creates a new instance ofaves it (to the JSON file) the id"""
        if not args:
            print("** class name missing **")
            return
        try:
            new_instance = eval(args)()
            storage.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")
            return

    def do_show(self, args):
        """Prints the string representation of an instance"""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        class_name, id_number = args[0], args[1]
        try:
            obj_dict = storage.all()
            if class_name not in obj_dict:
                print("** class doesn't exist **")
                return
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
        argl = args.split()
        if  len(argl) == 0:
            print("** class name missing **")
            return
        if len(argl) == 1:
            print("** instance id missing **")
            return
        class_name, id_number = argl[0], argl[1]
        dest = storage.all()
        keyc = f"{class_name}.{id_number}"         
        if class_name not in dest:
            print("** class doesn't exist **")
            return
        else:
            if id_number not in dest:
                print("** no instance found **")
                return
            if keyc in dest:
                del dest[keyc]
                storage.save()
            else:
                print("** no instance found **")
                return

    def do_all(self, args):
        """Prints all string representabased or not on the class name."""
        obj_dict = storage.all()
        if args:
            try:
                eval(args)
                fil_obj = []

                for key, obj in obj_dict.items():
                    if key.startswith(args):
                        fil_obj.append(str(obj))

                print(fil_obj)
            except NameError:
                print("** class doesn't exist **")
        else:
            all_objs = [str(obj) for obj in obj_dict.values()]
            print(all_objs)

    def do_update(self, args):
        """Updates on the class name and id by adding or updating attribute"""
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
        cl_name = args[0]
        obj_id = args[1]
        attr_name = args[2]
        attr_value = args[3].strip('"')
        try:
            obj_dict = storage.all()
            if cl_name not in obj_dict:
                print("** class doesn't exist **")
                return
            key = f"{cl_name}.{obj_id}"
            if key in obj_dict:
                obj = obj_dict[key]
                try:
                    attr_type = type(getattr(obj, attr_name))
                    attr_value = attr_type(attr_value)
                except AttributeError:
                    pass
                setattr(obj, attr_name, attr_value)
                obj.save()
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
