#get the line num -> run the file -> write the result in filename_result.txt
#how to run files in turn ? ->1. new code run   2. old code 
#new code : read file run it write result
#
from multiprocessing.pool import Pool
from multiprocessing import Process
import os,sys
from bpro_2 import subprocess_run
from bpro_2 import cmdname
import subprocess
import os, sys
import logging

list_bitop = ['and','nand','nor','or','xnor','xor']
list_arith = ['add','mul','sdiv','udiv','srem','urem','sub']
#list_bitop = ['and','nand','nor','or','xnor','xor']
#list_arith = ['add','mul','div','smod','rem','sub']
list_overflow = ['addo','divo','mulo','subo']
list_all = list_bitop + list_arith


def process(line):
    list_line = line.split()
    for i in list_line:
        if i in list_all:
            list_line.append('###UF###\n')
            linenum.append(k)#get the substitude line num
            line = ' '.join(list_line)
            #print('after process:',line)
            linechange.append(line)
    return line

def process_r(line):
    print(line)
    if (line == '0'):
        newline = 'timeout'
        print('timeout')
    elif('unknown' in line):
        newline = 'unknown'
    elif('sat' in line):
        newline = 'sat'
    else:
        newline = 'error'
        print('error')
    print(newline)
    return newline

def filesname(name):#new name for btorfiles 
    str_list = list(name)
    i = name.find('btor')
    del str_list[i-1 : -1]
    str_list.pop()
    newname = ''.join(str_list)
    return newname

def getfile0():
    with open(path,encoding='utf-8')as f:
        with open(root + '/'+ 'alladd','w',encoding='utf-8')as g:
            while True:
                line= f.readline()
                global k
                k += 1
                line = process(line)
                if not line:break
                g.write(line)

def getfile():
    with open(path ,encoding='utf-8')as f:
        line= f.readline()
        global k
        k += 1
        line = process(line)

def getfiles(bound):
    t = -1
    #print('this is linenum and linechange')
    #print(linenum,linechange)
    newname = filesname(name)
    with open(root + '/' + newname +'_res.txt' , 'w' ,encoding = 'utf-8') as r:
        for i in linenum:
            #part 1 : get one file
            t += 1
            with open(path ,encoding='utf-8')as f: 
                with open(root + '/help/'+ newname +'_' + str(t) + '.btor' ,'w',encoding='utf-8')as g:
                    print(root + '/help/'+ newname +'_' + str(t) + '.btor' )
                    global kk
                    kk = 0
                    while True:
                        line = f.readline()
                        kk += 1
                        if kk == i:
                            line = linechange[t]                    
                        if not line:break
                        g.write(line)
        #part 2: run this file 
            str_shell = '../build/pono --logging-smt-solver -k ' + str(bound) + ' ./crafted/cav14_example/cav14_example.btor2'    
            str_shell = cmdname(str_shell,root + '/help/'+ newname +'_' + str(t) + '.btor', bound)
            print(str_shell)
            line = p.apply_async(subprocess_run, args = (str_shell,)).get()
            line = str(linenum[t])+'  '+ process_r(line) +'\n'
            r.write(line)
        #part 3: write the result

def main():
    getfile0()
    getfiles(10)


if __name__=='__main__':
    p = Pool(1)
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            if(name.find('btor') >= 0):
                k=0
                linenum = []
                linechange = []
                path = os.path.join(root, name)
                main()
