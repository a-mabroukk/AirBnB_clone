#!/usr/bin/python3
"""importing cmd module"""

import cmd
import json

class HBNBCommand(cmd.Cmd):
    """class definition to create a command line interpreter that
    done by sub-classing the cmd.Cmd class"""

    prompt = "(hbnb) "
    """a custom prompt that issue a prompt, accept input and
    parse an initial prefix off the received input"""

    def do_quit(self, line):
        """provides the exit command to abort the interpreter"""
        return True

    def do_EOF(self, line):
        """An end-of-file on input"""
        print()
        return True

    def emptyline(self):
        """A method that can change the by default behavior
        of repeating the last command by overriding the emptyline method"""
        pass

    def do_create(self, o):
        """Creates a new instance of BaseModel"""
        try:
            isinstance(self, self.__class__.__name__)
        except NameError:
            print(f"** class name missing **")
        if self.__class__.__name__ is None:
            print(f"** class doesn't exist **")

    def do_show(self, o):
        """Prints the string representation of an instance 
        based on the class name and id"""
        try:
            isinstance(self, self.__class__.__name__)
        except NameError:
            print(f"** class name missing **")
        if self.__class__.__name__ is None:
            print(f"** class doesn't exist **")
        elif self.__class__.__name__.id is None:
            print(f"** instance id missing **")
        elif not self.__class__.__name__.id.exists():
            print(f"** no instance found **")

    def do_destroy(self, o):
        """ Deletes an instance based on the class name and id"""
        try:
            isinstance(self, self.__class__.__name__)
        except NameError:
            print(f"** class name missing **")
        if self.__class__.__name__ is None:
            print(f"** class doesn't exist **")
        elif self.__class__.__name__.id is None:
            print(f"** instance id missing **")
        elif not self.__class__.__name__.id.exists():
            print(f"** no instance found **")

    def do_all(self, o):
        """Prints all string representation of
        all instances based or not on the class name"""
        try:
            isinstance(self, self.__class__.__name__)
        except NameError:
            print(f"** class name missing **")
        return list(self)

    def do_update(self, o):
        """Updates an instance based on the class
        name and id by adding or updating attribute"""
        try:
            isinstance(self, self.__class__.__name__)
        except NameError:
            print(f"** class name missing **")
        if self.__class__.__name__ is None:
            print(f"** class doesn't exist **")
        elif self.__class__.__name__.id is None:
            print(f"** instance id missing **")
        elif not self.__class__.__name__.id.exists():
            print(f"** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
