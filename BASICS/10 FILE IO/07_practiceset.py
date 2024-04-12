with open("D:\\2024\\for python\\10 FILE IO\\hash.txt", "r") as f:
    content = f.read()

content = content.replace("donkey", "******")

with open("D:\\2024\\for python\\10 FILE IO\\hash.txt", "w") as f:
    f.write(content)
