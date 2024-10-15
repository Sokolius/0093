import pandas
from createpath import file_0093_path as f093p, file_1094_path as f94p

def readdata(path):
    pandas.set_option('display.max_columns',None)
 #   pandas.set_option('display.max_rows', None)
    df = pandas.read_csv(path,skiprows=6,sep=';',encoding='utf-8')
    df.rename(columns=df.iloc[0])
    df.drop(df.index[0])
   # df.drop(columns=['Unnamed: 1'],axis=1)
    emptycolum = df.columns.str.contains('^Unnamed') #список пустых(левых столбцов)
   # df = df.loc[:, df.columns.str.contains('^Unnamed')]
    lstindexcolemty = [i for i in range(len(emptycolum)) if emptycolum[i] == True]# лямбда для нахождения индексов столбцов из списка пустых столбцов
    df.drop(df.columns[lstindexcolemty],axis=1,inplace=True)
    return df

def readdatabr(path2):
    pandas.set_option('display.max_columns', None)
    pandas.set_option('display.max_rows', None)
    df = pandas.read_csv(path2, skiprows=5, sep=';', encoding='utf-8',on_bad_lines='skip')
    df.rename(columns=df.iloc[0])
    df.drop(df.index[0])
    # df.drop(columns=['Unnamed: 1'],axis=1)
    emptycolum = df.columns.str.contains('^Unnamed')  # список пустых(левых столбцов)
    # df = df.loc[:, df.columns.str.contains('^Unnamed')]
    lstindexcolemty = [i for i in range(len(emptycolum)) if
                       emptycolum[i] == True]  # лямбда для нахождения индексов столбцов из списка пустых столбцов
    df.drop(df.columns[lstindexcolemty], axis=1, inplace=True)
    return df
