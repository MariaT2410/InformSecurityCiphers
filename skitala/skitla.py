# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np;
import itertools;
import time;


# преобразование строки в матрицу (n m) reshape
def matrixnew(str, column, row):
    to_array = [char for char in str]
    
    matrix = np.reshape(to_array, (column, row));
    trans_matrix = matrix.transpose();
    #print(trans_matrix);
    concl=''
    for i in range( len(trans_matrix)):
        for j in range(len(trans_matrix[i])):
            concl=concl+trans_matrix[i][j];
    return concl;


# шифрование строки
def encrypt(str, column, row):
    strsecrypt ='';
    if (len(str) > column*row):
        strs = [str[i:i+column*row] for i in range(0, len(str), column*row)]
        #print(strs);
        for strindex in strs:
            #print(strindex);
            if (len(strindex) < column*row):
                star =column*row-len(strindex);
                for i in range(0, star):
                    strindex=strindex+"%";
                strecrypt= matrixnew(strindex, column, row);
            else:
                strecrypt= matrixnew(strindex, column, row);
            strsecrypt = strsecrypt+strecrypt;
        
    return strsecrypt;
 
 
 
# дешифрование 
def decrypt(strecrypt, column, row):
    strdeecrypt ='';
    if (len(strecrypt) > column*row):
        strs = [strecrypt[i:i+column*row] for i in range(0, len(strecrypt), column*row)]
        #print(strs);
        for strindex in strs:
            #print(strindex);
            strdeecrypt = strdeecrypt + matrixnew(strindex, row, column);
    return strdeecrypt;

    

def readFile(name):
    file=open(name)
    text = file.read()
    file.close()
    return text    
    
def writeFile(text, name):
    file=open(name, 'w')
    file.write(text)
    file.close()
    
    
    
# массив всевозможных пар ключей(n m) в диапазоне range(12,37):   
def getKeys():
    listed=[];
    ls=[];
    for a in range(12,37):
        for i in range(2, a // 3):
            if (a % i== 0):
                ls.append(a)
        listed= list(set(ls))
    keys_m_n =[]
    for i in range(0, len(listed)):
        primeNum = []
        for num in range(1, listed[i]+1):
            if(listed[i]%num==0):
                if(num!=1 and num!=listed[i]):
                    primeNum.append(num)
    
        com_set = itertools.combinations(primeNum, 2)
        for couple in com_set: 
            if couple[0]*couple[1]==listed[i]:
                reverse_couple=(couple[1], couple[0])
                keys_m_n.append(couple)
                keys_m_n.append(reverse_couple)
    return keys_m_n
    

# поиск ключа для дешифрования и расчет времени на это
def decryptGetKeys(text, encrypttext, n_m):
    start = time.perf_counter()
    exp=len(text)-len(encrypttext)  
    numer=1;
    for i in n_m:
        print(i);
        if(len(encrypttext)%(i[0]*i[1])==0):
            decrypttext = decrypt(encrypttext, i[0], i[1]);
            if(decrypttext[:exp] == text):
                stop = time.perf_counter();
                filename ="newDecrypttext.txt"
                writeFile(decrypttext, filename)
                print( "Text ", stop-start)
                numer+=1;
                
    
  

nm=getKeys();
print(nm)   
    

strin = 'Hello_world!myfrens';
m = 4;#column
n = 3
print(strin);
print(encrypt(strin, m, n));
s =encrypt(strin, 2, 3);
#print(decrypt(encrypt(strin, m, n), m, n));
newsecr = decryptGetKeys(strin, s, getKeys());
print(newsecr)



text1=readFile('.../text1.txt')
print(len(text1));
m1 = 4 #число столбцов
n1 = 6 # число строк
encrypted1 = encrypt(text1, m1, n1)
writeFile(encrypted1, '.../text1encrypted.txt')
decrypted1 = decrypt(encrypted1, m1, n1)
writeFile(decrypted1, '.../text1endecrypted.txt')
newdecrypted1 = decryptGetKeys(text1, encrypted1, nm)
#print(newdecrypted1)


text2=readFile('.../text2.txt')
print(len(text2));
m2 = 3 #число столбцов
n2 = 6 # число строк
encrypted2 = encrypt(text2, m2, n2)
writeFile(encrypted2, '.../text2encrypted.txt')
decrypted2 = decrypt(encrypted2, m2, n2)
writeFile(decrypted2, '.../text2endecrypted.txt')
newdecrypted1 = decryptGetKeys(text2, encrypted2, nm)
#print(newdecrypted1)


text3=readFile('.../text3.txt')
print(len(text3));
m3 = 4 #число столбцов
n3 = 3 # число строк
encrypted3 = encrypt(text3, m3, n3)
writeFile(encrypted3, '.../text3encrypted.txt')
decrypted3 = decrypt(encrypted3, m3, n3)
writeFile(decrypted3, '.../text3endecrypted.txt')
newdecrypted1 = decryptGetKeys(text3, encrypted3, nm)
#print(newdecrypted1)



text4=readFile('.../text4.txt')
print(len(text4));
m4 = 4 #число столбцов
n4 = 8 # число строк
encrypted4 = encrypt(text4, m4, n4)
writeFile(encrypted4, '.../text4encrypted.txt')
decrypted4 = decrypt(encrypted4, m4, n4)
writeFile(decrypted4, '.../text4endecrypted.txt')
newdecrypted1 = decryptGetKeys(text4, encrypted4, nm)
#print(newdecrypted1)



text5=readFile('.../text5.txt')
print(len(text5));
m5 = 4 #число столбцов
n5 = 3 # число строк
encrypted5 = encrypt(text5, m5, n5)
writeFile(encrypted5, '.../text5encrypted.txt')
decrypted5 = decrypt(encrypted5, m5, n5)
writeFile(decrypted5, '.../text5endecrypted.txt')
newdecrypted1 = decryptGetKeys(text5, encrypted5, nm)
#print(newdecrypted1)