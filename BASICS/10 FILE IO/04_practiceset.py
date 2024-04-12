# write a program to read the text from a given file 'poems.txt' and find out whether it contains the word 'twinkle'

with open('D:\\2024\\for python\\10 FILE IO\\poem.txt','r') as f:
    read = f.read()
if 'twinkle' in read:
    print("It contains twinkle word in it")
else:
    print("Twinkle is not present")