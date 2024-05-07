import pandas as pd
import numpy as np
import requests, xmltodict, json, time
from requests.exceptions import ConnectionError


# 크롤링 후 csv파일 다운로드 함수
def trans_csv(df, name):
    df.to_csv(name + '.csv', encoding='utf-8-sig', index=False)


## 0. API 기본 정보
key = '0443949103'
url = f'https://data.ex.co.kr/openapi/restinfo/restBestfoodList?key={key}'


## 1. 자동화 함수
def auto_req(numOfRows):
    page_no = 1
    df_list = []

    while True:
        try:
            params = {'serviceKey': key, 'pageNo': page_no, 'numOfRows': numOfRows, 'type': 'xml'}  # 대상별 정보 파라미터

            response = requests.get(url, params=params)
            xml_data = response.text
            xml_parse = xmltodict.parse(xml_data)
            xml_dict = json.loads(json.dumps(xml_parse))

            print()
            print('item',xml_dict['data'])
            print(int(xml_dict['data']['pageNo']), int(xml_dict['data']['pageSize']))
            print(int(xml_dict['data']['pageNo']) > int(xml_dict['data']['pageSize']))

            if xml_dict['data'] == None:
                break

            elif int(xml_dict['data']['pageNo']) > int(xml_dict['data']['pageSize']):
                print("true")
                break

            else:
                item_list = xml_dict['data']['list']
                df = pd.json_normalize(item_list)
                df_list.append(df)
                print(df_list)


            page_no += 1  # 페이지 증가

        except Exception as e :
            print('error', e)
            time.sleep(10)

    return(df_list)

## 2. API 호출
df_list = auto_req(10)  #실행 전 함수에서 해당파라미터 주석 풀기
base_df = df_list[0]  #concat 할 가장 첫번째 df

#--호출한 df 모두 concat
for i in range(1, len(df_list)):
    con_df = df_list[i]
    base_df = pd.concat([base_df, con_df])
df = pd.concat(df_list)

print(df)

# csv 저장
trans_csv(df, '음식점정보')
