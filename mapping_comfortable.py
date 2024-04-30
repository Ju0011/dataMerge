import numpy as np
import requests, xmltodict, json
import pandas as pd

base_df = pd.read_csv("휴게소_만족도_매핑.csv")
copy_df = base_df.copy()

add_df = pd.read_csv("data/휴게소_만족도_20171231.csv", encoding='cp949')

copy_df['satisfaction'] = ''
success_1 = 0

for i in range(len(copy_df)):
    for j in range(len(add_df)):
        try:
            if copy_df['sliced_rest'][i] == add_df['휴게소명'][j]:
                # 3. 컬럼 내용 매핑
                if add_df['평가등급'][j] == '최우수':
                    copy_df['satisfaction'][i] = 2
                elif add_df['평가등급'][j] == '우수':
                    copy_df['satisfaction'][i] = 1
                else:
                    copy_df['wifi'][i] = 0

                success_1 += 1
                print(f"나머지 {i}번째 {success_1}건 성공")
            else:
                pass
        except:
            continue

copy_df.to_csv('휴게소_만족도_매핑.csv', encoding='utf-8-sig',index=False)