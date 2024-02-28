#!/usr/bin/python3
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from model import storage

class HBNBCommand(cmd.Cmd):
  propmt "(hbnb) "
  valid_classes = ["BaseModel", "User"]



def emptyline(self):
  """
  Do Nothing when an empty line is entered
  """
  pass

def do EOF(self,line):
  """
  Hand the End-of-File (Ctrl+D) event to exit the program
  """
  return True

def do_quit(self, arg)
  """
  Quit the program
  """
  return True

def do_create(self, arg)
  """
  Create a new instance of BaseModel and save it to the JSON file.
  Usage: create <class_name>
  """
  commands = shlex.split(arg)

  if len(commands) == 0:
    print("** class name missing**")
  elif commands[0] not in self.valid_classes:
    print("** class doesn't exist**")
  else:
      new instance = BaseModel ()
      new_instance.save()
      print(new_instance.id)
