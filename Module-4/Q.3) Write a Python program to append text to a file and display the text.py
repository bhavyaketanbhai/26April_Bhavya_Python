with open('filename.txt', 'a') as file:
    file.write('This is some new text!\n')

with open('filename.txt', 'r') as file:
    data = file.read()
    print(data)