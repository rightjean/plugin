import pandas as pd
import matplotlib.pyplot as plt

# 데이터 로드
df = pd.read_csv('./1시간_단위_강서희망점.csv')

# 컬럼 이름 변경
df.columns = ['Date', 'Power_Actual', 'Power_Simulation']

# 인덱스를 Date로 설정
df_1 = df.set_index('Date')

# Date 인덱스를 datetime 형식으로 변환
df_1.index = pd.to_datetime(df_1.index)

# 데이터프레임을 일 단위로 변환
df_daily = df_1.resample('D').sum()

# 난방 시즌과 냉방 시즌 정의
heating_season = (df_daily.index.month == 12) | (df_daily.index.month <= 2)
cooling_season = (df_daily.index.month >= 3) & (df_daily.index.month <= 11)

# 난방 시즌 데이터
heating_df = df_daily[heating_season]

# 냉방 시즌 데이터
cooling_df = df_daily[cooling_season]

# 난방 시즌과 냉방 시즌 시뮬레이션 데이터 시각화
plt.plot(heating_df.index, heating_df['Power_Simulation'], label='Heating Season Simulation Power', color='blue')
plt.plot(cooling_df.index, cooling_df['Power_Simulation'], label='Cooling Season Simulation Power', color='red')
plt.xlabel('Date')
plt.ylabel('Power Simulation')
plt.title('Heating vs Cooling Season - Simulation Power')
plt.legend()
plt.show()