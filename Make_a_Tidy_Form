from urllib.parse import quote_plus
from string import ascii_uppercase
import pandas as pd

file_name = '總統-A05-4-候選人得票數一覽表-各投開票所(臺北市).xls'
file_url = quote_plus(file_name)
spreadsheet_url = "https://taiwan-election-data.s3-ap-northeast-1.amazonaws.com/presidential_2020/{}".format(file_url)
presidential = pd.read_excel(spreadsheet_url, skiprows=[0, 1, 3, 4], thousands=',')

n_cols = presidential.columns.size
n_candidate = n_cols-11
idvars=['town', 'village', 'office']
candidate = list(presidential.columns[3:(3+n_candidate)])
office = list(ascii_uppercase[:8])
columns = idvars+candidate+office
presidential.columns = columns

presidential_filna = presidential.fillna(method='ffill')
presidential_dropna = presidential_filna.dropna()

df_presidential = pd.melt(presidential_dropna, id_vars=idvars, var_name='candidate', value_name='vote')
print(df_presidential)
