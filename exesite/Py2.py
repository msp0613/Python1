def write():
    file = open("data.txt", "w")
    input_user = ''
    print("Wprowadz dane")
    while(input_user != 'end'):
        input_user = input()
        file.write(input_user + "\n")
    file.close()

def read():
    file = open("data.txt", 'r')
    data = file.readlines()
    print(data)


read()