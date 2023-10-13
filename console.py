#!/usr/bin/python3

"""this is a command console to test our models"""

import cmd
from models import storage
from models import cls_names

class HBNBCommand(cmd.Cmd):
    """this class to make command line interpreter"""

    prompt = '(hbnb) '

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
        line = arg.split()
        if (len(line) == 0):
            print("** class name missing **")
        elif line[0] not in cls_names:
            print("** class doesn't exist **")
        else:
            new_instance = cls_names[line[0]]()
            print(new_instance.id)
            storage.new(new_instance)
            storage.save()

    def do_show(self, arg):
        """this command shows an instance\n"""
        prs_cmd = arg.split()
        if (len(prs_cmd) == 0):
            print("** class name missing **")
            return
        if prs_cmd[0] not in cls_names:
            print("** class doesn't exist **")
            return
        if (len(prs_cmd) < 2):
            print("** instance id missing **")
            return

        key = prs_cmd[0] + '.' + prs_cmd[1]
        if key in storage.all():
            print(storage.all()[key])
            return

        print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        """
        line = arg.split()
        if not line or len(line) == 0:
            print("** class name missing **")
            return
        if line[0] not in cls_names:
            print("** class doesn't exist **")
            return
        if len(line) < 2:
            print("** instance id missing **")
            return

        key = line[0] + '.' + line[1]
        if key in storage.all():
            del storage.all()[key]
            storage.save()
            return
        print("** no instance found **")

    def do_all(self, arg):
        """ Prints all string representation of all instances
            based or not on the class name.
        """
        line = arg.split()
        l = []
        if len(line) != 0 and line[0] not in cls_names:
            print("** class doesn't exist **")
            return
        for key, value in storage.all().items():
            if len(line) == 0:
                l.append(value.__str__())
            elif line[0] in key:
                l.append(value.__str__())
        print(l)

    def do_update(self, arg):
        """ Updates an instance based on the class name and id
            by adding or updating attribute.

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        line = arg.split()
        if len(line) == 0:
            print("** class name missing **")
            return
        if line[0] not in cls_names:
            print("** class doesn't exist **")
            return
        if len(line) < 2:
            print("** instance id missing **")
            return
        else:
            key = line[0] + '.' + line[1]
            if key not in storage.all():
                print("** no instance found **")
                return
        if len(line) < 3:
            print("** attribute name missing **")
            return
        if len(line) < 4:
            print("** value missing **")
            return
        setattr(storage.all()[key], line[2], line[3][1:-1])
        storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
