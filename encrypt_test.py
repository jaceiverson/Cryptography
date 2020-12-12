import numpy as np

def encrypt(text,key):
    pass

def decrypt(text,key):
    buckets=len(text)//key
    decode=''
    code=[]
    for i in range(0,len(text),buckets):
        code.append(text[::-1][i:i+buckets])
                    
    for x in range(buckets):
        for y in code:
            decode+=y[x]

    return decode

def j_encrypt(steps,text):
    
    text_l=chunks(text,steps)
    msg=''
    for x in range(steps):
        
        for y in text_l:
            try:
                msg+=(y[x])
            except IndexError:
                msg+='#'
        
    return msg[::-1]

def chunks(l,n):
    #this function groups a list into sections of n length
    #for our purposes, we want 5
    return [l[i:i + n] for i in range(0, len(l), n)]


j='do you want to break in tonight'
code=4
f=j_encrypt(4,j)
