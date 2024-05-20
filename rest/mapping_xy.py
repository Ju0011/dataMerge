import numpy as np
import requests, xmltodict, json
import pandas as pd

base_df = pd.read_csv("휴게소_필요데이터.csv")
copy_df = base_df.copy()

add_df = pd.read_csv("/Users/parkjuyoung/Desktop/dataMerge/data/휴게소정보_20210809.csv", encoding='cp949')

copy_df['latitude'] = ''    #위도
copy_df['longitude'] = ''   #경도
success_1 = 0

for i in range(len(copy_df)):
    for j in range(len(add_df)):
        try:
            if copy_df['sliced_rest'][i] == add_df['휴게소명'][j]:
                # 3. 컬럼 내용 매핑
                copy_df['latitude'][i] = add_df['위도'][j]
                copy_df['longitude'][i] = add_df['경도'][j]

                success_1 += 1
                print(f"나머지 {i}번째 {success_1}건 성공")
            else:
                pass
        except:
            continue

copy_df.to_csv('휴게소_위도경도.csv', encoding='utf-8-sig',index=False)