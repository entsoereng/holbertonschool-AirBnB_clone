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
