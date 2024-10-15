from wreadfile import readdata, readdatabr as rdbr
import pandas
from getdata import redfile as date93

def mod(path,path2):
    df = readdata(path)
    econrequirid = df[df["№ банка"].str.contains("Требования к экономике").fillna(False)].index
    econrequirtable = df.iloc[econrequirid[0] + 1:econrequirid[0] + 4]

    kgprequirid = df[df["№ банка"].str.contains("Требования к KГП").fillna(False)].index
    kgprequirtable = df.iloc[kgprequirid[0] + 1:kgprequirid[0] + 4]

    chasektrequirid = df[df["№ банка"].str.contains("Требования к частному сектору").fillna(False)].index
    chasektrequirtable = df.iloc[chasektrequirid[0] + 1:chasektrequirid[0] + 4]

    nebfinrequirid = df[df["№ банка"].str.contains("Требования к небанковским финансовым организациям").fillna(False)].index
    nebfinrequirtable = df.iloc[nebfinrequirid[0] + 1:nebfinrequirid[0] + 4]

    fizlicrequirid = df[df["№ банка"].str.contains("Требования к физическим лицам").fillna(False)].index
    fizlicrequirtable = df.iloc[fizlicrequirid[0] + 1:fizlicrequirid[0] + 4]
    dfclear = pandas.concat(
        [econrequirtable, kgprequirtable, chasektrequirtable, nebfinrequirtable, fizlicrequirtable], axis=0)
    dfbr = modbr(path2)
    dfbr.index = dfbr.index+1
    dfclear['ОАО "Банк развития Республики Беларусь"'] = dfbr['ОАО "Банк развития Республики Беларусь"']
    dfclear.rename(columns={'ОАО "Банк развития Республики Беларусь"':'222'},inplace=True)
    print(dfclear)
    return  dfclear

def modbr(path2):
    df = rdbr(path2)
    econrequirid = df[df.iloc[:,0].str.contains("Требования к экономике").fillna(False)].index
    econrequirtable = df.iloc[econrequirid[0] + 1:econrequirid[0] + 4]

    kgprequirid = df[df.iloc[:, 0].str.contains("Требования к KГП").fillna(False)].index
    kgprequirtable = df.iloc[kgprequirid[0] + 1:kgprequirid[0] + 4]

    chasektrequirid = df[df.iloc[:, 0].str.contains("Требования к частному сектору").fillna(False)].index
    chasektrequirtable = df.iloc[chasektrequirid[0] + 1:chasektrequirid[0] + 4]

    nebfinrequirid = df[df.iloc[:, 0].str.contains("Требования к небанковским финансовым организациям").fillna(False)].index
    nebfinrequirtable = df.iloc[nebfinrequirid[0] + 1:nebfinrequirid[0] + 4]

    fizlicrequirid = df[df.iloc[:, 0].str.contains("Требования к физическим лицам").fillna(False)].index
    fizlicrequirtable = df.iloc[fizlicrequirid[0] + 1:fizlicrequirid[0] + 4]
    dfclear = pandas.concat(
        [econrequirtable, kgprequirtable, chasektrequirtable, nebfinrequirtable, fizlicrequirtable], axis=0)
    return dfclear

def cleaningdata(path,path2):
    df = mod(path,path2)
    df.drop(columns=df.columns[0], axis=1, inplace=True)
    df = df.fillna(0)
    for column in df:
        df[column] = df[column].str.replace(" ","")
        df[column] = df[column].str.replace(",", ".")
        df[column] = df[column].str.replace("\n", "")
        df[column] = df[column].str.replace("\t", "")
    df = df.astype(float)
    listcol = df.columns.tolist()
    df = df.T # transpose daframe
    df.insert(0,"date",date93(path,path2),False)
    df.insert(0, "bank", listcol, False)
    prod_list = df.values.tolist()
    print(prod_list)
    return prod_list
