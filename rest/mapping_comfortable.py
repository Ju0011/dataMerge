import numpy as np
import requests, xmltodict, json
import pandas as pd

base_df = pd.read_csv("휴게소_만족도_매핑.csv")
copy_df = base_df.copy()

add_df = pd.read_csv("data/휴게소정보_20210809.csv", encoding='cp949')

copy_df['electric_car'] = ''
copy_df['nursing_room'] = ''
copy_df['pharmacy'] = ''
success_1 = 0

for i in range(len(copy_df)):
    for j in range(len(add_df)):
        try:
            if copy_df['sliced_rest'][i] == add_df['휴게소명'][j]:
                # 3. 컬럼 내용 매핑
                if add_df['전기차충전소유무'][j] == 'Y':
                    copy_df['electric_car'][i] = 1
                elif add_df['전기차충전소유무'][j] == 'N':
                    copy_df['electric_car'][i] = 0

                if add_df['약국유무'][j] == 'Y':
                    copy_df['pharmacy'][i] = 1
                elif add_df['약국유무'][j] == 'N':
                    copy_df['pharmacy'][i] = 0

                if add_df['수유실유무'][j] == 'Y':
                    copy_df['nursing_room'][i] = 1
                elif add_df['수유실유무'][j] == 'N':
                    copy_df['nursing_room'][i] = 0


                success_1 += 1
                print(f"나머지 {i}번째 {success_1}건 성공")
            else:
                pass
        except:
            continue

copy_df.to_csv('휴게소_시설_매핑.csv', encoding='utf-8-sig',index=False)