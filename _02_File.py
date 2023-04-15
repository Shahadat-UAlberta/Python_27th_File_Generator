file = open("demo.txt", "r")

file_content = file.read()

new_content = file_content.replace("Hello Java!", "Hello C++")

file.close()

file = open("demo.txt", "w")
file.write(new_content)
file.close()
