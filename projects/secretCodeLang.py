# Python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Program asks whether you want to code or decode

import string
import random

#for 3 random letters
# print("".join((random.choice(string.ascii_letters)) for x in range(3)))

msg= input("Enter the message\n")
quest=input(''' press 'e' for encoding the message 
                 OR
enter 'd' for decing the message\n ''')
if (quest== "e"):
    coding=True
elif(quest== "d"):
    coding=False
else:
    print("press e or d ")

words=msg.split(" ")
# print(words)
new_words = [] 
if (coding):
    for word in words:
        if(len(word)>=3):
            r1= "".join((random.choice(string.ascii_letters)) for x in range(3))
            r2= "".join((random.choice(string.ascii_letters)) for x in range(3))
            new_word = r1 + word[1:] + word[0] + r2
            new_words.append(new_word)
        else:
            new_words.append(word[::-1])
    print(" ".join(new_words))
else:
    for word in words:
        if(len(word)>=3):
            new_word = word[-4] + word[3:-4]
            new_words.append(new_word)
        else:
            new_words.append(word[::-1])
    print(" ".join(new_words))



