
def Write_File(path,line,mode):
    try:
       
        file = open(path,mode)
        file.writelines(line)
        file.writelines("\n")
        file.close()
        pass
    except:
        pass

def Read_File(path):  
    try:
        print('READING_FILE_AT:',path)
        file = open(path,'r',encoding="utf8")
        strs = file.readlines()
        strs = ' '.join(strs)
        #file.close()
        return strs
    except:
        pass
    
