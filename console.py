#!/usr/bin/python3
"""importing cmd module"""

import cmd


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
