
import pandas as pd
import json

import numpy as np
import requests, xmltodict, json
import pandas as pd

base_df = pd.read_csv("휴게소_위도경도.csv")
data = base_df.copy()


for i in range(len(data)):
    if data['wifi'][i] == 'TRUE':
        data['wifi'][i] == 1>0
    else:
        data['wifi'][i] == 1<0



    if data['electric_car'][i] == 'TRUE':
        data['electric_car'][i] == 1>0
    else:
        data['electric_car'][i] == 1<0



    if data['nursing_room'][i] == 'TRUE':
        data['nursing_room'][i] == 1>0
    else:
        data['nursing_room'][i] == 1<0



    if data['pharmacy'][i] == 'TRUE':
        data['pharmacy'][i] == 1>0
    else:
        data['pharmacy'][i] == 1<0


    if data['Braile_block'][i] == 'TRUE':
        data['Braile_block'][i] == 1>0
    else:
        data['Braile_block'][i] == 1<0


    if data['pet'][i] == 'TRUE':
        data['pet'][i] == 1>0
    else:
        data['pet'][i] == 1<0

data.to_csv('휴게소_booltype.csv', encoding='utf-8-sig',index=False)