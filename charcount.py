n = int(input("enter no. of strings"))

dict = {}
for i in range(n):
    j = input(f"enter string {i+1}")
    dict[i] = [1+len(j), j]

for i in dict:
    print(f"{dict[i][0]}{dict[i][1]}", end = '')