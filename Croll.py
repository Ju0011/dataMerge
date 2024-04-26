import pandas as pd
import numpy as np
import requests, xmltodict, json,  time
from requests.exceptions import ConnectionError

#크롤링 후 csv파일 다운로드 함수
def trans_csv(df, name):

    df.to_csv(name + '.csv', encoding='utf-8-sig', index=False)



## 0. API 기본 정보
key = '0443949103'
url = 'https://data.ex.co.kr/openapi/restinfo/hiwaySvarInfoList?key=0443949103&type=xml'


## 1. 자동화 함수
def auto_req( numOfRows ):
    page_no = 1
    df_list = []

    #값 저장할 리스트 변수 만들기

    while True:
        params = {'key': key, 'pageNo': page_no, 'numOfRows': numOfRows, 'type' : 'xml' } # 대상별 정보 파라미터
        #params = {'serviceKey' : key, 'returnType' : 'xml', 'numOfRows' : numOfRows, 'pageNo' : page_no}  # 대상별 정보 파라미터

        response = requests.get(url, params=params)
        xml_data = response.text
        xml_parse = xmltodict.parse(xml_data)
        xml_dict = json.loads(json.dumps(xml_parse))


        if xml_dict['svarGsstClssNm'] == '주유소':
            break
        else:
            item_list = xml_dict['response']['body']['items']['item']
            df = pd.json_normalize(item_list)
            df_list.append(df)

        print(page_no)
        page_no += 1 #페이지 증가

    return(df_list)



## 2. API 호출
df_list = auto_req(100)  #실행 전 함수에서 해당파라미터 주석 풀기
base_df = df_list[0]  #concat 할 가장 첫번째 df

#--호출한 df 모두 concat
for i in range(1, len(df_list)):
    con_df = df_list[i]
    base_df = pd.concat([base_df, con_df])





# csv 저장
trans_csv(base_df, 'hiwaySvarInfoList')