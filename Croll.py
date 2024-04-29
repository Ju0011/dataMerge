import pandas as pd
import numpy as np
import requests, xmltodict, json, time
from requests.exceptions import ConnectionError


# 크롤링 후 csv파일 다운로드 함수
def trans_csv(df, name):
    df.to_csv(name + '.csv', encoding='utf-8-sig', index=False)


## 0. API 기본 정보
key = '0443949103'
url = 'https://data.ex.co.kr/openapi/restinfo/hiwaySvarInfoList?key=0443949103&type=xml'


## 1. 자동화 함수
def auto_req(numOfRows):
    page_no = 1
    df_list = []

    # 값 저장할 리스트 변수 만들기
    params = {'key': key, 'pageNo': page_no, 'numOfRows': numOfRows, 'type': 'xml'}  # 대상별 정보 파라미터

    response = requests.get(url, params=params)
    xml_data = response.text
    xml_parse = xmltodict.parse(xml_data)
    xml_dict = json.loads(json.dumps(xml_parse))

    item_list = xml_dict['data']['list']
    df = pd.json_normalize(item_list)
    df_list.append(df)
    return (df_list)

## 2. API 호출
df_list = auto_req(1)

df = pd.concat(df_list)

# 값이 1인 행 삭제
for i in range(1,len(df)):
    df = df[df['svarGsstClssCd'] != '1']

# csv 저장
trans_csv(df, 'hiwaySvarInfoList_주유소제거')
