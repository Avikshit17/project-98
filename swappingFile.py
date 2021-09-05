def swapFileData():
    f1=open("sample1.txt","r+")
    f2=open("sample2.txt","r+")
    data_a=f1.read()
    data_b=f2.read()
    f1.write(data_b)
    f2.write(data_a)
swapFileData()
    
