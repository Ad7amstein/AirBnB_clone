#!/usr/bin/python3

"""this is a command console to test our models"""

import cmd
import models

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
        if (len(arg) == 0):
            print("** class name missing **")
        elif ("BaseModel" != arg):
            print("** class doesn't exist **")
        else:
            new_instance = models.base_model.BaseModel()
            print(new_instance.id)
            new_instance.save()

    def do_show(self, arg):
        """this command shows an instance\n"""
        prs_cmd = arg.split()
        if (len(prs_cmd) == 0):
            print("** class name missing **")
            return
        elif(prs_cmd[0] != "BaseModel"):
            print("** class doesn't exist **")
            return
        elif(len(prs_cmd) < 2):
            print("** instance id missing **")
            return
        
        flag = 0
        #key = prs_cmd[0] + '.' + prs_cmd[1]
        for value in models.storage.all().values():
            if prs_cmd[1] == value.id:
                print(value)
                flag = 1
        if flag != 1:
            print("** no instance found **")



if __name__ == '__main__':
    HBNBCommand().cmdloop()
