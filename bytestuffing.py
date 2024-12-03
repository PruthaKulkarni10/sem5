data = input("enter data")
start = input("enter starting delimiter")
end = input("enter ending delimiter")
escape = input("enter escape char")

stuffed_data = start
for i in data:
    if i==start or i==end or i==escape:
        stuffed_data+=escape
    stuffed_data+=i
stuffed_data+=end

print(stuffed_data)