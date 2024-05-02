import numpy as np
import requests, xmltodict, json
import pandas as pd

base_df = pd.read_csv("주유소_휴게소코드_완료.csv")
copy_df = base_df.copy()

add_df = pd.read_csv("C:/Users/admin/Desktop/data/dataMerge/data/전기차 수소차 충전소 현황(2023년).csv", encoding='cp949')
copy_df['electric'] = ''
copy_df['hydrogen'] = ''

success_1 = 0
for i in range(len(copy_df)):
    for j in range(len(add_df)):
        try:
            if copy_df['serviceAreaName'][i] == add_df['주유소명'][j]:
                # 컬럼 내용 매핑
                if add_df['전기차 충전소'][j] == 'O':
                    copy_df['electric'][i] = 1
                elif add_df['전기차 충전소'][j] == 'X':
                    copy_df['electric'][i] = 0
                
                if add_df['수소차 충전소'][j] == 'O':
                    copy_df['hydrogen'][i] = 1
                elif add_df['수소차 충전소'][j] == 'X':
                    copy_df['hydrogen'][i] = 0

                success_1 += 1
                print(f"나머지 {i}번째 {success_1}건 성공")
            else:
                pass
        except:
            continue

copy_df.to_csv('주유소_전기수소_완료.csv', encoding='utf-8-sig',index=False)
