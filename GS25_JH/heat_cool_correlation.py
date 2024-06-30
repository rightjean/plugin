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
heating_season = df_1[(df_1.index.month <= 2) | (df_1.index.month == 12)]
cooling_season = df_1[(df_1.index.month >= 3) & (df_1.index.month <= 11)]

# 난방,냉방 시즌 데이터
df_daily_heating = heating_season.resample('D').sum()
df_daily_cooling = cooling_season.resample('D').sum()

# 난방,냉방 시즌 데이터
# heating_df = df_daily[heating_season]
# cooling_df = df_daily[cooling_season]

# 난방,냉방 시즌 상관계수 계산
heating_correlation = df_daily_heating['Power_Simulation'].corr(df_daily_heating['Power_Actual'])
cooling_correlation = df_daily_cooling['Power_Simulation'].corr(df_daily_cooling['Power_Actual'])


# 난방,냉방 시즌 산점도
plt.scatter(df_daily_heating['Power_Simulation'], df_daily_heating['Power_Actual'], color='blue')
plt.scatter(df_daily_cooling['Power_Simulation'], df_daily_cooling['Power_Actual'], color='red')

print("Power_Actual와 Power_Simulation 간의 상관계수", 
      "\nHeating Season", heating_correlation,
      "\nCooling Season", cooling_correlation,)


plt.xlabel('Daily Power_Simulation')
plt.ylabel('Daily Power_Actual')
plt.title('Daily Heating and Cooling Season: Simulation vs Actual Power')
plt.legend()
plt.show()
