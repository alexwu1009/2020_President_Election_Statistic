import pandas as pd
import numpy as np

df = pd.read_csv('presidential.csv')
county_type=df['county'].map(lambda x:'六都' if x in {'臺北市', '桃園市', '臺中市', '新竹市', '臺南市', '高雄市'} else '非六都')
df['county']=county_type
presidential=df.groupby(['county', 'candidate'])['votes'].sum()
presidential = pd.DataFrame(presidential)
presidential = presidential.reset_index()

print(presidential)
