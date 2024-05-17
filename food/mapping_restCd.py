import numpy as np
import requests, xmltodict, json
import pandas as pd

base_df = pd.read_csv("음식_칼럼제거.csv", encoding='cp949')
copy_df = base_df.copy()

add_df = pd.read_csv("/Users/parkjuyoung/Desktop/dataMerge/rest/휴게소_완료.csv")
copy_df['svarCd'] = ''
# 'serviceAreaName' 칼럼에서 '주유소' 단어 제거하여 'restNm' 칼럼에 추가
copy_df['slide_RestNm'] = copy_df['stdRestNm'].str.replace('휴게소', '')

success_1 = 0
for i in range(len(copy_df)):
    for j in range(len(add_df)):
        try:
            if copy_df['slide_RestNm'][i] == add_df['sliced_rest'][j]:
                # 컬럼 내용 매핑
                copy_df['svarCd'][i] = add_df['svarCd'][j]

                success_1 += 1
                print(f"나머지 {i}번째 {success_1}건 성공")
            else:
                pass
        except:
            continue

copy_df.to_csv('음식점_휴게소코드_완료.csv', encoding='utf-8-sig',index=False)
