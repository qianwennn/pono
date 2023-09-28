#!/usr/bin/python
import subprocess
import sys
import logging
import os

gameproc = "../build/pono -k 50 --smt-solver cvc5 ./crafted/crafted/counter/counter.btor2"

def getPid(gameproc):
    cmd = "ps aux| grep '%s'|grep -v grep " % gameproc
    logging.info(cmd)
    out = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
    infos = out.stdout.read().splitlines()
    #print(infos)
    if len(infos) >= 1:
        for i in infos:
            pid = i.split()[1]
        return pid
    else:
        return -1

def reducepid(line):
    str_list = list(line)
    del str_list[0 : 2]
    str_list.pop()
    newline = ''.join(str_list)
    return newline

def delpid():
    pid = getPid(gameproc)
    pid = str(pid)
    pid = reducepid(pid)
    cmd = 'kill -9 '+pid
    print(cmd)
    subprocess.run(args=cmd,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,universal_newlines=True,timeout=5,check=False)


delpid()


