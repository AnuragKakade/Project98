def swapingFiles():
    f1=input("name of the file1 ")
    f2=input("name of the file2 ")
    with open(file1, 'r') as a:
        data_a = a.read()
            with open(file2, 'r') as b:
                data_b = b.read()
    with open(file1, 'w') as a:
        a.write(data.b)
