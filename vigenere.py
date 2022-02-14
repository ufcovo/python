#Mert Bulut and Selin Ulusoy.
import re #This is a regular expression. This for searching.
import string

alphabets = "abcçdefgğhıijklmnoöpqrsştuüvwxyz" # this is the english and turkish letters

def encrypt(p, k):   #p is the plain text, k is the key
    c = ""
    cindex = [] # return the index of characters ex: if k='e' then cindex= 7
    for x in k:
        cindex.append(alphabets.find(x))
    i = 0
    for x in p:
      if i == len(cindex):
          i = 0
      pos = alphabets.find(x) + cindex[i] #to find the index of the character and perform the shift with the key
      #print(pos)
      if pos > 31:
          pos = pos-32               # to check exceed the limit
      c += alphabets[pos].capitalize()  #the cipher text will be capital letters
      i += 1
    return c

def decrypt(c, k): # c is the cipher text, k is the key
    p = ""
    cindex = []
    for x in k:
        cindex.append(alphabets.find(x))
    i = 0
    for x in c:
      if i == len(cindex):
          i = 0
      pos = alphabets.find(x.lower()) - cindex[i]
      if pos < 0:
          pos = pos + 32
      p += alphabets[pos].lower()
      i +=1
    return p
try:
    print("This is a vigenere cipher.\n"
          "Press 1 to Enrypt a message \nPress 2 to Decrypt a message")
    choose = input("Choice: ")
    if choose == '1':
       p = input("Enter the text: ")
       p = p.replace(" ", "")  # this will make sure that there is no space in the message
       if p.isalpha():
           k = input("Enter the key: ")
           k = k.strip()  # remove the white spaces from both sides
           if k.isalpha():
              # print(k)
               c = encrypt(p, k)
               print("The cipher text is: ", c)

           else:
               print(k)
               print("Enter valid key, key is only one character word!")
       else:
           print("Only letters are allowed !!")

    elif choose == '2':
        c = input("Enter the cipher text: ")
        c = c.replace(" ", "")
        if c.isalpha():
            k = input("Enter the key: ")
            if not k.isalpha():
                print("Enter valid key, key is only one character word!")
            else:
                p = decrypt(c, k)
                print("The plain text is: ", p)
        else:
            print("Only letters are allowed!")

    else:
        print("Please enter a valid choice!")
except Exception as e:
    print(e)
    exit("Enter a valid text please! ")