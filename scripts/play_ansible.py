#!/usr/local/bin/python
# coding:utf-8
import os
import sys
import commands
import getpass
import context
import subprocess

def check_appstore_id():
  try_count = 0
  appstore_id = ""
  while not appstore_id and try_count < 3:
    appstore_id = raw_input("Please input App Store Id: ")
    try_count += 1
  if not appstore_id:
    print "Please input correct App Store Id"
    sys.exit(1)
  return appstore_id

#def check_password():
#  try_count = 0
#  appstore_pw = ""
#  while not appstore_pw and try_count < 3:
#    appstore_pw = getpass.getpass("Please input App Store Password: ")
#    try_count += 1
#  if not appstore_pw:
#    print "Please input correct App Store Password"
#    sys.exit(1)
#  return appstore_pw

appstore_id = check_appstore_id()
#appstore_pw = check_password()

dir_path = context.PROVISIONING_HOME + "/provisioning"
os.chdir(dir_path)
cmd = "ansible-playbook site.yml --connection=local --extra-vars \"appstore_id=" + appstore_id + "\""
print cmd
#cmd_id = "appstore_id=" + appstore_id
#cmd_pw = "appstore_password=" + appstore_pw
p = ""
try:
  if __name__ == '__main__':
    for line in context.get_lines(cmd):
        sys.stdout.write(line)
#     res = subprocess.check_output(cmd, shell=True)
#    res = subprocess.check_output(["ansible-playbook", "site.yml", "--connection=local", "--extra-vars", cmd_id, cmd_pw])
except (KeyError, ValueError) as err:
    logger.exception('Error dosomething: %s', err)
print p

