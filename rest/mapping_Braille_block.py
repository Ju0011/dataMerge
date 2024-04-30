import numpy as np
import requests, xmltodict, json
import pandas as pd

base_df = pd.read_csv("휴게소_시설_매핑.csv")
copy_df = base_df.copy()

add_df = pd.read_excel("data/장애인 안내시설 설치현황(2020년).xlsx")
print(add_df)
copy_df['Braile_block'] = ''
success_1 = 0

for i in range(len(copy_df)):
    for j in range(len(add_df)):
        try:
            if copy_df['sliced_rest'][i] == add_df['휴게소명'][j]:
                print(copy_df['sliced_rest'][i], add_df['휴게소명'][j])
                copy_df['Braile_block'][i] = 1

                success_1 += 1
                print(f"나머지 {i}번째 {success_1}건 성공")

            else:
                pass
        except:
            continue

copy_df.to_csv('휴게소_완료.csv', encoding='utf-8-sig',index=False)