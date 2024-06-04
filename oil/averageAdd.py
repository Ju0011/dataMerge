import numpy as np
import pandas as pd

base_df = pd.read_csv("주유소_형변환.csv")
copy_df = base_df.copy()

copy_df['diselAver'] = ''
copy_df['gasolineAver'] = ''
copy_df['lpgAver'] = ''

# 칼럼에서 0이 아닌 값들만 필터링
non_zero_disel = copy_df[copy_df['diselPrice'] != 0]['diselPrice']
non_zero_gasoline = copy_df[copy_df['gasolinePrice'] != 0]['gasolinePrice']
non_zero_lgpg = copy_df[copy_df['lpgPrice'] != 0]['lpgPrice']


# 칼럼의 평균을 계산
disel_Aver = non_zero_disel.mean()
gasol_Aver = non_zero_gasoline.mean()
lpg_Aver = non_zero_lgpg.mean()

# 평균과 반올림값
print(f"디젤의 평균 값: {disel_Aver}, {np.round(disel_Aver,-1)}")
copy_df['diselAver'] = np.round(disel_Aver,-1)

print(f"가솔린의 평균 값: {gasol_Aver}, {np.round(gasol_Aver,-1)}")
copy_df['gasolineAver'] = np.round(gasol_Aver,-1)

print(f"lpg 의 평균 값: {lpg_Aver}, {np.round(lpg_Aver,-1)}")
copy_df['lpgAver'] = np.round(lpg_Aver,-1)

copy_df.to_csv('주유소_평균값.csv', encoding='utf-8-sig',index=False)
