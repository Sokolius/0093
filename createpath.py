import os
import sys

path = "//rootfs4/Data/GUOFR/URL/IAS/"
max_day_in_i = os.listdir(path)# спиок папок в директ
max_day_in_i = sorted(max_day_in_i,reverse=True)# сортировка списка
max_day_in_i = max_day_in_i[0:5]# выбираем нужную папку (2 в нашем случае) т.к. отчет падает день в день
listtab93 =[]
listtab94 = []
for fday in max_day_in_i:
    work_folder = path+fday
    work_folder_path = os.listdir(work_folder)
    file_0093_path = ""# workfile
    file_1094_path =""
    counter = 0
    for i in work_folder_path:
        if i[0:10] == "s01BAL0093":
            file_0093_path = work_folder + "/"+i
            listtab93.append(file_0093_path)
            continue
        elif i[0:10] == "s01BAL1094":
            file_1094_path = work_folder + "/"+i
            listtab94.append(file_1094_path)
            continue
        elif len(work_folder) != counter:
            counter+=1
            if len(work_folder)==counter:
                print("Файла в папке нет/ не был еще выгружен")
                sys.exit()# завершаем работу скрипта так как файла нет
listtab93.reverse()
listtab94.reverse()
print(listtab93)
print(listtab94)