dev_list = []
file = open("devices.txt", "r")
for i in file:
    i = i.strip()
    #print(i)
    dev_list.append(i)
file.close()

for i in dev_list:
    print(i)