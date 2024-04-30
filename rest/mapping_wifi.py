import numpy as np
import requests, xmltodict, json
import pandas as pd

base_df = pd.read_csv("data/hiwaySvarInfoList_주유소제거.csv")
copy_df = base_df.copy()

add_df = pd.read_csv("data/wifi_2023.csv", encoding='cp949')

copy_df['sliced_rest'] = copy_df['svarNm'].str.replace('휴게소', '')
copy_df['wifi'] = ''
success_1 = 0

for i in range(len(copy_df)):
    for j in range(len(add_df)):
        try:
            if copy_df['sliced_rest'][i] == add_df['휴게소명'][j]:

                # 3. 컬럼 내용 매핑
                if add_df['가능여부'][j] == 1:
                    print('true')
                    copy_df['wifi'][i] = 1

                else:
                    copy_df['wifi'][i] = 0

                success_1 += 1
                print(f"나머지 {i}번째 {success_1}건 성공")
            else:
                pass
        except:
            continue

copy_df.to_csv('휴게소_와이파이_매핑.csv', encoding='utf-8-sig',index=False)