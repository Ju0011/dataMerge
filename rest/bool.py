import numpy as np
import requests, xmltodict, json
import pandas as pd

base_df = pd.read_csv("휴게소_완료.csv")
copy_df = base_df.copy()

add_df = pd.read_csv("C:/Users/admin/Desktop/data/dataMerge/animal/반려동물_휴게소코드_완료.csv", encoding='cp949')
print(add_df)
copy_df['pet'] = ''

success_1 = 0

for i in range(len(copy_df)):
    for j in range(len(add_df)):
        try:
            if copy_df['svarCd'][i] == add_df['svarCd'][j]:
                copy_df['pet'][i] = 'true'

                success_1 += 1
                print(f"나머지 {i}번째 {success_1}건 성공")

            else:
                pass
        except:
            continue

for i in range(len(copy_df)):
    if copy_df['wifi'][i] == 1:
        copy_df['wifi'][i] = 'true'
    else:
        copy_df['wifi'][i] = 'false'

    if copy_df['electric_car'][i] == 1:
        copy_df['electric_car'][i] = 'true'
    else:
        copy_df['electric_car'][i] = 'false'


    if copy_df['nursing_room'][i] == 1:
        copy_df['nursing_room'][i] = 'true'
    else:
        copy_df['nursing_room'][i] = 'false'

    if copy_df['pharmacy'][i] == 1:
        copy_df['pharmacy'][i] = 'true'
    else:
        copy_df['pharmacy'][i] = 'false'


    if copy_df['Braile_block'][i] == 1:
        copy_df['Braile_block'][i] = 'true'
    else:
        copy_df['Braile_block'][i] = 'false'


copy_df.to_csv('휴게소_boolean.csv', encoding='utf-8-sig',index=False)