import os,sys
import subprocess

list_bitop = ['and','nand','nor','or','xnor','xor']
list_arith = ['add','mul','div','smod','rem','sub']
list_overflow = ['addo','divo','mulo','subo']
list_all = list_bitop + list_arith + list_overflow


def process(line):
    list_line = line.split()
    for i in list_line:
        if i in list_all:
            list_line.append('###UF###\n')
            linenum.append(k)
            line = ' '.join(list_line)
            #print('after process:',line)
            linechange.append(line)
    return line

def filesname(name,t):
    b = '_'+ str(t)
    str_list = list(name)
    i = name.find('btor')
    str_list.insert(i-1,b)
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

def getfiles():
    t = -1
    print('this is linenum and linechange')
    print(linenum,linechange)
    for i in linenum:
        t += 1
        with open(path ,encoding='utf-8')as f: 
            newname = filesname(name , t)
            with open(root + '/'+ newname,'w',encoding='utf-8')as g:
                global kk
                kk = 0
                while True:
                    line = f.readline()
                    kk += 1
                    if kk == i:
                        line = linechange[t]                    
                    if not line:break
                    g.write(line)


def main():
    getfile0()
    getfiles()


if __name__=='__main__':
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            if(name.find('btor') >= 0):
                k=0
                linenum = []
                linechange = []
                path = os.path.join(root, name)
                print(path)
                main()

