#!/usr/bin/python3

"""this is a command console to test our models"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """this class to make command line interpreter"""

    prompt = '(hbnb) '
    cls_names = ["BaseModel"]

    def do_EOF(self, arg):
        """end of a file terminates the program\n"""
        return (True)

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return (True)

    def emptyline(self):
        """do not do anything\n"""
        pass

    def do_create(self, arg):
        """this command creates a new instance of a class\n"""
        if (len(arg) == 0):
            print("** class name missing **")
        elif arg not in self.cls_names:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            print(new_instance.id)
            new_instance.save()

    def do_show(self, arg):
        """this command shows an instance\n"""
        prs_cmd = arg.split()
        if (len(prs_cmd) == 0):
            print("** class name missing **")
            return
        elif prs_cmd[0] not in self.cls_names:
            print("** class doesn't exist **")
            return
        elif (len(prs_cmd) < 2):
            print("** instance id missing **")
            return

        for value in storage.all().values():
            if prs_cmd[1] == value.id:
                print(value)
                return

        print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        """
        line = arg.split()
        if not line or len(line) == 0:
            print("** class name missing **")
            return
        elif line[0] not in self.cls_names:
            print("** class doesn't exist **")
            return
        elif len(line) < 2:
            print("** instance id missing **")
            return

        for key, value in storage.all().items():
            if value.id == line[1]:
                del storage.all()[key]
                storage.save()
                return
        print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
