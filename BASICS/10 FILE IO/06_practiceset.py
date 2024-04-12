for i in range(2, 21):
    with open(f"D:\\2024\\for python\\10 FILE IO\\table/MULTIPLICATION_OF_{i}.txt", "w") as f:
        for j in range(1, 11):
            f.write(f"{i} X {j} = {i*j}\n")
