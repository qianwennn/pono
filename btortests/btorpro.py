list_bitop = ['and','nand','nor','or','xnor','xor']
list_arith = ['add','mul','div','smod','rem','sub']
list_overflow = ['addo','divo','mulo','subo']
list_all = list_bitop + list_arith + list_overflow + ['is']
k=0
t= -1
linenum = []
linechange = []

def process(line):
    list_line = line.split()
    for i in list_line:
        if i in list_all:
            list_line.append('###UF###\n')
            linenum.append(k)
            line = ' '.join(list_line)
            print('after process:',line)
            linechange.append(line)
    return line
                            
def getfile():
    with open(s + '/'+ s +'.btor2',encoding='utf-8')as f:
        with open(s + '/'+ s + '_x.btor2','w',encoding='utf-8')as g:
            while True:
                line= f.readline()
                global k
                k += 1
                line = process(line)
                if not line:break
                g.write(line)

def getfiles():
    print(linenum,linechange)
    for i in linenum:
        global t
        t += 1
        with open(s + '/'+ s + '.btor2',encoding='utf-8')as f: 
            with open(s + '/'+ s + '_'+str(t)+'.btor2','w',encoding='utf-8')as g:
                global kk
                kk = 0
                while True:
                    line = f.readline()
                    kk += 1
                    if kk == i:
                        print(i,linechange[t])
                        line = linechange[t]                    
                    if not line:break
                    g.write(line)
            
def main():
    getfile()
    getfiles()


if __name__=='__main__':
    s = 'cav14_example'
    main()           
            
    
