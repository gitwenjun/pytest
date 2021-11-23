import csv
def csv_bing_wds(file):
    mylist = []
    with open(file,'r',encoding='utf8') as f:
        data = csv.reader(f)

        for i in data:
            mylist.append(i)
        del mylist[0]
        return mylist