import numpy as np
import requests, xmltodict, json
import pandas as pd

base_df = pd.read_csv("C:/Users/admin/Desktop/data/dataMerge/data/주유소실시간.csv")
copy_df = base_df.copy()

add_df = pd.read_csv("C:/Users/admin/Desktop/data/dataMerge/rest/휴게소_완료.csv")

# 'serviceAreaName' 칼럼에서 '주유소' 단어 제거하여 'restNm' 칼럼에 추가
copy_df['restNm'] = copy_df['serviceAreaName'].str.replace('주유소', '')

copy_df.to_csv('주유소가격_칼럼추가.csv', encoding='utf-8-sig',index=False)

success_1 = 0
copy_df['svarCd'] = ''
for i in range(len(copy_df)):
    for j in range(len(add_df)):
        try:
            if copy_df['restNm'][i] == add_df['sliced_rest'][j]:
                # 컬럼 내용 매핑
                copy_df['svarCd'][i] = add_df['svarCd'][j]

                success_1 += 1
                print(f"나머지 {i}번째 {success_1}건 성공")
            else:
                pass
        except:
            continue

copy_df.to_csv('주유소_휴게소코드.csv', encoding='utf-8-sig',index=False)
