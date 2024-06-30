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

# Simulation과 Actual Power
plt.figure()
plt.scatter(df_1['Power_Simulation'], df_1['Power_Actual'])
plt.xlabel('Power Simulation')
plt.ylabel('Power Actual')
plt.title(f'Simulation vs Actual Power')
plt.grid(True)
plt.show()

# 데이터프레임을 일 단위로 변환
df_daily = df_1.resample('D').sum()
plt.figure()
plt.scatter(df_daily['Power_Simulation'], df_daily['Power_Actual'])
plt.xlabel('Daily Power Simulation')
plt.ylabel('Daily Power Actual')
plt.title('Daily Simulation vs Actual Power')
plt.grid(True)
plt.show()

# 난방 시즌과 냉방 시즌 정의
heating_season = (df_1.index.month >= 11) | (df_1.index.month <= 3)
cooling_season = (df_1.index.month >= 6) & (df_1.index.month <= 9)

# 난방 시즌 데이터
heating_df = df_1[heating_season]

# 냉방 시즌 데이터
cooling_df = df_1[cooling_season]

# 난방 시즌 데이터 시각화
plt.figure()
plt.plot(heating_df.index, heating_df['Power_Actual'], label='Actual Power')
plt.plot(heating_df.index, heating_df['Power_Simulation'], label='Simulation Power', alpha=0.7)
plt.xlabel('Date')
plt.ylabel('Power')
plt.title('Heating Season - Actual vs Simulation Power')
plt.legend()
plt.grid(True)
plt.show()

# 냉방 시즌 데이터 시각화
plt.figure()
plt.plot(cooling_df.index, cooling_df['Power_Actual'], label='Actual Power')
plt.plot(cooling_df.index, cooling_df['Power_Simulation'], label='Simulation Power', alpha=0.7)
plt.xlabel('Date')
plt.ylabel('Power')
plt.title('Cooling Season - Actual vs Simulation Power')
plt.legend()
plt.grid(True)
plt.show()

# 실제 값과 시뮬레이션 값의 차이를 계산하여 기타 설비 및 조명의 전력 사용량을 추정
df_1['Power_Difference'] = df_1['Power_Actual'] - df_1['Power_Simulation']

# 기타 설비 및 조명 전력 사용량 시각화
plt.figure()
plt.plot(df_1.index, df_1['Power_Difference'], label='Equipment and Lighting Power')
plt.xlabel('Date')
plt.ylabel('Power Difference')
plt.title('Equipment and Lighting Power Usage')
plt.legend()
plt.grid(True)
plt.show()
