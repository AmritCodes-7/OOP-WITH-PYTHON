# detecting spam comments
text = input("Enter a text:")
spam = False

if("money"in text):
    spam = True
elif("rope" in text):
    spam = True
else:
    spam = False

if(spam):
    print("TEXT IS SPAM")
else:
    print("Text is not a spam")