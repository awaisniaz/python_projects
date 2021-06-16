def openFile():
    file = open('index.txt','rb')
    print(file.read())
    try:
        print(10/2)
    except ZeroDivisionError as e:
        print(e)
    else:
        print("I am Always Excute")

openFile()