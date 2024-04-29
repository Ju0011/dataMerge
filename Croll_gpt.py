import pandas as pd
import xml.etree.ElementTree as ET
import numpy as np
import requests, xmltodict, json,  time

key = '0443949103'
url = 'https://data.ex.co.kr/openapi/restinfo/hiwaySvarInfoList?key=0443949103&type=xml'

# XML 데이터를 파싱하여 딕셔너리에 저장하는 함수
def parse_xml(xml_string):
    root = ET.fromstring(xml_string)
    data = {'svarGsstClssNm': [], 'svarNm': [], 'svarAddr': []}
    for item in root.findall('.//list'):
        svarGsstClssNm = item.find('svarGsstClssNm').text
        if svarGsstClssNm != '주유소':  # '주유소'인 데이터는 제외
            data['svarGsstClssNm'].append(svarGsstClssNm)
            data['svarNm'].append(item.find('svarNm').text)
            data['svarAddr'].append(item.find('svarAddr').text)
    return data

def auto_req( numOfRows ):
    page_no = 1
    df_list = []

    #값 저장할 리스트 변수 만들기

    while True:
        params = {'key': key, 'pageNo': page_no, 'numOfRows': numOfRows, 'type' : 'xml' } # 대상별 정보 파라미터

        response = requests.get(url, params=params)
        xml_data = response.text
        xml_parse = xmltodict.parse(xml_data)
        xml_dict = json.loads(json.dumps(xml_parse))

        print(xml_dict)
        return xml_dict

xml_string = auto_req(100)

# XML 파싱 후 데이터프레임으로 변환
data = parse_xml(xml_string)
df = pd.DataFrame(data)

# 엑셀 파일로 저장
df.to_excel('output.xlsx', index=False)
