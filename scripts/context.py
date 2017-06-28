#!/usr/local/bin/python
# coding:utf-8
import os
import subprocess

PROVISIONING_HOME = os.path.dirname(os.path.dirname(__file__))

def print_context():
  print '======================='
  print 'Print context variables.'
  print '-----------------------'
  print 'PROVISIONING_HOME: PROVISIONING_HOME'
  print '======================='

def tag_echo (script, msg):
  print '[' + script + ']' + msg

def get_lines(cmd):
    '''
    :param cmd: str 実行するコマンド.
    :rtype: generator
    :return: 標準出力 (行毎).
    '''
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    while True:
        line = proc.stdout.readline()
        if line:
            yield line

        if not line and proc.poll() is not None:
            break
