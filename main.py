import os
from file_process import*
from data_process import*
from pathlib import Path
from tkinter import *

def main():
  
    #Lấy đường dẫn:
    #path_input = Path.cwd()
    
    path_input = input("Root Data Input : ")
   
    path_output = input("Root Data Output :")

   
    
    #Lấy danh sách các file trong thư mục Input(Dữ Liệu Đầu Vào)
    file_data = [ path_input + "/"+ f for f in os.listdir(path_input)]
    print('FIle : ',file_data)
    
    #Tạo Thư Mục Đầu Ra:
    #os.mkdir(path_input + "/" + "Output" , 1)
    # if(not Path(path_input + "/Output").exists()):
    #    os.mkdir("Output")
  

    # list_path = []
    # for (root, dirs, files) in os.walk(path_):
    #     print("Root = ",root)
    #     for file in files:
    #         list_path.append(root + "/" + file)

    # print(list_path)
  
  
    for item in file_data:
        #Dữ Liệu Thô:
        source = Read_File(item)
        name = item.replace(path_input + "/" ,'').split('.')
        path_output = path_output + "/"
        #Dữ Liệu Sau Khi Loại Bỏ Các Tag HTLM:
        source = clean_html(source)
        name_clean_html = name[0] + '_after_clean_html' + '.' +name[1]
        Write_File( path_output + name_clean_html  ,source,'w')
        #Dữ Liệu Sau Khi Loại Bỏ Khoảng Trắng Và Các Kí Tự Đặc Biệt:
        clean_source = remove_special_character(source)
        name_clean_character = name[0] + '_after_remove_special_character' + '.' + name[1]
        Write_File(path_output + name_clean_character, clean_source,'w')
        #List Các Câu Đã Tách:
        sents = sentences_separated(clean_source)
        name_sents = name[0] + '_after_sentences_sparated' + '.' + name[1]
        for s in sents :
            Write_File(path_output + name_sents,s,'a')
        #Lish Các Từ Đã Tách:
        words = words_separated(clean_source)
        name_words = name[0] + '_after_words_sparated' + '.' + name[1]
        for w in words:
            Write_File(path_output + name_words, w,'a')
        #Dict Thông Kê Số Lượng Từ:
        words_new = word_statistical(words)
        name_words_statisical = name[0] + '_after_words_statistical' + '.' + name[1]

        for w in words_new:
            Write_File(path_output + name_words_statisical, w['word'] + " -- "+ str(w['count']) , 'a')

if __name__ == "__main__":
    main()
