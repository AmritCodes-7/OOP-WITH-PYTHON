class Number:
    def __init__(self, num) -> None:
        self.num = num

    def __add__(self, num2):
        print("lets add")
        return 3000


n1 = Number(4)
n2 = Number(5)
sum = n1 + n2
print(sum)
