import subprocess
import os, sys

def subprocess_run(str_shell):
    CompletedProcessObject=subprocess.run(args=str_shell,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,universal_newlines=True,timeout=10,check=False)
    if CompletedProcessObject:
        code,out,err=CompletedProcessObject.returncode,CompletedProcessObject.stdout,CompletedProcessObject.stderr
        #print(code)
        return out


def filesname(name,path):
    str_list = list(name)
    i = name.find('cvc5')
    del str_list[i+5: -1]
    str_list.pop()
    str_list.insert(i+6,path)
    newname = ''.join(str_list)
    return newname

def reduce(line):
    str_list = list(line)
    i = line.find('here')
    del str_list[0 : i+4]
    str_list.pop()
    str_list.pop()
    str_list.pop()
    newline = ''.join(str_list)
    return newline

def runfile():
    str_shell='../build/pono --smt-solver  cvc5  ./crafted/cav14_example/cav14_example.btor2'
    #subprocess_run(str_shell)
    with open('./result.txt','w',encoding='utf-8')as g:
        for root, dirs, files in os.walk(".", topdown=False):#get btor files
            for name in files:
                if(name.find('btor') >= 0):
                    path = os.path.join(root, name)
                    line = name
                    g.write(line)
                    str_shell = filesname(str_shell,path) #run btor files
                    print(str_shell)
                    line = subprocess_run(str_shell)
                    line = reduce(line)
                    print(line)
                    g.write(line + '\n')#add the resut into file
                        
    
def main():
    runfile()


#runcmd(["cd crafted","ls"])#序列参数
if __name__=='__main__':
    main()

