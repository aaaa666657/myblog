# encoding: utf-8
import pandas as pd
url = "https://www.iecs.fcu.edu.tw/teacher/陳烈武/class/" 
dfs = pd.read_html(url)  ## 回傳DataFrame類別的陣列
df  = dfs[1]
#df  = [ row[1:] for row in df.values.tolist()]
print(df)
