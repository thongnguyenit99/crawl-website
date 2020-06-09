import re 
from string import punctuation #Tập dấu câu từ thư viện string
import nltk
from nltk.corpus import stopwords #import tập hư từ 
from nltk.tokenize import word_tokenize,sent_tokenize #Hàm xử lý tách từ tách câu 
from bs4 import BeautifulSoup
from file_process import*



def print_data(data):
    for item in data:
        print(item , end = '\n')
        print("*"*20)
############################## Hàm Làm Sạch Dữ Liệu ##############################
def clean_html(text):
    soup = BeautifulSoup(text,'html.parser')
    return soup.get_text()
############################## Hàm Xóa Các Kí Tự Thừa ##############################
def remove_special_character(text):
    #Xóa cá kí tự đặc biệt
    string = re.sub('[^\w\s\.]',' ',text)
    #Xóa các kí tự khoảng trắng ở trong chuỗi
    string = re.sub('\s+',' ',string)
    #Xóa kí tự khoảng trắng đầu cuối chuỗi
    string = string.strip()
    return string

############################## Hàm Tách Câu ##############################
#Danh Sách Hư Từ
my_stopwords = set(stopwords.words('english') + list(punctuation))
my_stopwords.add('..')
def sentences_separated(text):
    return  sent_tokenize(text)

############################## Hàm Tách Từ Và Bỏ Hư Từ ##############################
def words_separated(text):
    #Tách Từ
    words = word_tokenize(text)
    #Đưa về in thường
    words = [w.lower() for w in words]
    #Loại bỏ hư từ
    words = [w for w in words if w not in my_stopwords]
    return words

############################## Hàm Thống Kê Số Lượng Từ  ##############################
def word_statistical(words):
    word_dict = []
    words_new = set(words)
    for w in words_new:
        data = {'word' : w,'count': words.count(w)}
        word_dict.append(data)
    return word_dict

