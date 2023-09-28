def filesname(name):#new name for btorfiles 
    str_list = list(name)
    i = name.find('btor')
    del str_list[i-1 : -1]
    str_list.pop()
    newname = ''.join(str_list)
    return newname

name = 'help.btor'
line = filesname(name)
print(line)