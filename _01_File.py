
data = open("demo.txt")
print(data.read())
data.close()


with open("demo.txt") as data:
    print(data)
    print(data.read())
