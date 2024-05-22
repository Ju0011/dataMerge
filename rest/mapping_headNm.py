import numpy as np
import requests, xmltodict, json
import pandas as pd

base_df = pd.read_csv("휴게소_위도경도.csv")
copy_df = base_df.copy()

add_df = pd.read_csv("휴게소_완료.csv")

copy_df['hdqrCd'] = ''
success_1 = 0

for i in range(len(copy_df)):
    for j in range(len(add_df)):
        try:
            if copy_df['sliced_rest'][i] == add_df['sliced_rest'][j]:
                # 3. 컬럼 내용 매핑
                copy_df['hdqrCd'][i] = add_df['hdqrCd'][j]


                success_1 += 1
                print(f"나머지 {i}번째 {success_1}건 성공")
            else:
                pass
        except:
            continue

copy_df.to_csv('휴게소_본부코드.csv', encoding='utf-8-sig',index=False)