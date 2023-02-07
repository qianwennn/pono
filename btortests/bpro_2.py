import subprocess
import os, sys

def subprocess_run(str_shell):
    try:
        CompletedProcessObject=subprocess.run(args=str_shell,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,universal_newlines=True,timeout=10,check=False)
        if CompletedProcessObject:
            code,out,err=CompletedProcessObject.returncode,CompletedProcessObject.stdout,CompletedProcessObject.stderr
            #print(code)
            return out
    except:
        print('this file timeout')
        return 0 

        


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
    str_shell='../build/pono -k 20 --smt-solver  cvc5  ./crafted/cav14_example/cav14_example.btor2'
    #subprocess_run(str_shell)
    btornames = []
    filenames = ['paper_v3','sw_loop','cav14_example','sw_state_machine','sw_ball2004_1','counter','sw_sym_ex','client_server','eq_sdp_v4','eq_sdp_v6']
    with open('./result.txt','w',encoding='utf-8')as g:
        with open('./finres.txt','w',encoding='utf-8')as k:
            for root, dirs, files in os.walk(".", topdown=False):#get btor files
                for name in files:
                    if(name.find('btor') >= 0):
                        path = os.path.join(root, name)
                        line = name
                        g.write(line)#get name of btoor2file to be tested
                        for i in filenames:                       
                            if i in line:
                                print(i)
                                try:
                                    if(i == filename):
                                        fileamount += 1
                                        filename = i
                                    else:
                                    #  print('the fileamount is:',fileamount)
                                    #  print('the covered is:',cover)
                                    #  print('the unknown is:',unknown)
                                        line = filename+'\n'
                                        k.write(line)
                                        line = 'the fileamount is:'+ str(fileamount-1)+'\n'
                                        k.write(line)
                                        line = 'the covered is:'+ str(cover) +'\n'
                                        k.write(line)
                                        line = 'the unknown is:'+ str(unknown-1)+'\n'
                                        k.write(line)
                                        filename = i
                                        fileamount = 1
                                        cover = 0
                                        unknown = 0
                                except:
                                    filename = i
                                    fileamount = 1
                                    cover = 0
                                    unknown = 0                                
                                str_shell = filesname(str_shell,path) #run btor files
                                line = subprocess_run(str_shell)
                                if (line == 0):
                                    line = str(0)
                                else:
                                    print(line)
                                    line = reduce(line)
                                # print(line)    
                                if 'unknown' in line:
                                    unknown += 1
                                if 'is_covered: 1' in line:
                                    cover += 1
            line = filename+'\n'
            k.write(line)
            line = 'the fileamount is:'+ str(fileamount-1)+'\n'
            k.write(line)
            line = 'the covered is:'+ str(cover) +'\n'
            k.write(line)
            line = 'the unknown is:'+ str(unknown-1)+'\n'
            k.write(line)                
            g.write(line + '\n')#add the resut into file
                        
    
def main():
    runfile()


#runcmd(["cd crafted","ls"])#序列参数
if __name__=='__main__':
    main()

