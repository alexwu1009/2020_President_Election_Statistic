from string import ascii_uppercase
import pandas as pd
import numpy as np

data_report = pd.read_excel('總統-A05-4-候選人得票數一覽表-各投開票所(新北市).xls', skiprows=[0, 1, 3, 4], thousands=',')

#算出個欄位數量
#把各欄位分開整理
n_cols = data_report.columns.size
n_candidates = n_cols - 11
id_vars = ['town', 'village', 'office']                    #前三欄
candidates = list(data_report.columns[3:(3+n_candidates)]) #候選人欄位
office_cols = list(ascii_uppercase[:8])                    #後8欄位
col_names = id_vars + candidates + office_cols             #統整欄位
data_report.columns = col_names                            #設定欄位狀態

filled_na = data_report.fillna(method='ffill')             #因欄位有大量NaN，依依填補起來，系統會偵測上一個row是什麼而往下填補不用一個一個填上該區域名稱
df = data_report.assign(town=filled_na)

df = df.dropna()                                           #刪除多餘NaN值
df['town'].unique()
strip_str = df['town'].str.replace('\u3000', '')
df = df.assign(town=strip_str)                             #更新欄位（直接覆蓋）
df['town'].unique()

df = df.drop(labels=office_cols, axis=1)
                                                           #整理所有欄位並輸出
df = pd.melt(df, id_vars=id_vars, var_name='candidate_info', value_name='votes')  
print(df)
