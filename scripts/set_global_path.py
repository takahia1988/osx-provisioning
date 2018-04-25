#!/usr/bin/env python
import commands
import logging
import os
import sys
import getpass
import context
import subprocess

def isExistStringInFile(searchString, filePath):
  ld = open(filePath)
  lines = ld.readlines()
  ld.close()
  for line in lines:
    if line.find(searchString) >= 0:
        return true
  return false

fish_set_cmd = "echo `which fish` | sudo tee -a /etc/shells"
fish_set_path = ""
rbenv_set_cmd = "echo `which fish` | tee -a ~/.bash_profile"
rbenv_set_path = ""
pyenv_set_cmd = "echo `which fish` | tee -a ~/.bash_profile"
pyenv_set_path = ""
print cmd
try:
  if __name__ == '__main__':
    for line in context.get_lines(fish_cmd):
        sys.stdout.write(line)
    for line in context.get_lines(rbenv_cmd):
        sys.stdout.write(line)
    for line in context.get_lines(pyenv_cmd):
        sys.stdout.write(line)
except (KeyError, ValueError) as err:
    logger.exception('Error dosomething: %s', err)

