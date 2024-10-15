from createpath import file_0093_path as f93p
import csv
import datefinder

def redfile(path,path2):
    headlist = []
    with open(path,"r",encoding='utf-8') as file:
        file_r = csv.reader(file,delimiter=";")
        for row in file_r:
            headlist.append(row)
    headlist = headlist[1:2] # Delete empty strings
    headlist =list(filter(None, headlist[0]))
    dateinfile = list(datefinder.find_dates(headlist[0],first='day'))
    return dateinfile[0].date()

