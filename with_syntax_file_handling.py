with open("sample.txt","r")as f:
    data=f.read()
    print(data)
    f.close()

with open("sample.txt","w")as f:
    data=f.write("I hope you are doing well")
    print(data)
    f.close()