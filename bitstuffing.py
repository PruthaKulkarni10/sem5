data = input("enter data")

i=count = 0
while i<len(data):
    print(data[i], end='')
    if (data[i]=='1'):
        count+=1
        if count == 5:
            print(0, end='')
            count = 0
    else:
        count = 0

    i+=1