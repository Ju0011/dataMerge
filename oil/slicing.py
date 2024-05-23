import numpy as np
import requests, xmltodict, json
import pandas as pd

base_df = pd.read_csv("주유소_전기수소_최종완료.csv")
copy_df = base_df.copy()

success_1 = 0

def convert_to_int(price_str):
    if price_str == 'X':
        return price_str
    else:
        # '원' 제거
        price_str = price_str.replace('원', '')
        # 쉼표 제거
        price_str = price_str.replace(',', '')
    # 정수형으로 변환
    return int(price_str)


for i in range(len(copy_df)):
    copy_df['diselPrice'][i] = convert_to_int(copy_df['diselPrice'][i])
    copy_df['gasolinePrice'][i] = convert_to_int(copy_df['gasolinePrice'][i])
    copy_df['lpgPrice'][i] = convert_to_int(copy_df['lpgPrice'][i])


copy_df.to_csv('주유소_형변환.csv', encoding='utf-8-sig',index=False)
