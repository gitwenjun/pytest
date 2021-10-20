import csv
mylist = []
def parses_csv(file):
    with open(file,'r',encoding='utf8') as f:
        data = csv.reader(f)
        for i in data:
            mylist.append(i)
        del mylist[0]
        return mylist
