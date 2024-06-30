import pandas as pd
import matplotlib.pyplot as plt
plt.ion() # 그래프 한번에 표시

# 데이터 프레임 만들기
df = pd.read_csv('./1시간 단위 고양원당로점.csv')

## 데이터 레코드의 변경
df.columns = ['Date', 'Power', 'Simulation', 'Heat', 'Cool']

# 인덱스를 Date로 활용
df_1 = df.set_index('Date')

# Date 인덱스를 datetime 인덱스로 변환
df_1.index = pd.to_datetime(df_1.index)

df_daily = df_1.resample("D").sum() # 1일 단위 데이터를 sum 형태로 결합하겠다.
correlation = df_daily['Simulation'].corr(df_daily['Power'])

## 원하는 날짜 범위 추출
# Heating Season : 1월부터 2월, 12월
Heating_Season = df_1[(df_1.index.month <= 2) | (df_1.index.month == 12)]
# Cooling Season : 3월부터 11월
Cooling_Season = df_1[(df_1.index.month >= 3) & (df_1.index.month <= 11)]

df_daily_heating = Heating_Season.resample('D').sum()
df_daily_cooling = Cooling_Season.resample('D').sum()

correlation_heating = df_daily_heating['Simulation'].corr(df_daily_heating['Power'])
correlation_cooling = df_daily_cooling['Simulation'].corr(df_daily_cooling['Power'])

print("Power와 Simulation 간의 상관계수 (상관계수가 0.5 이상이면, 상관성이 있다고 판단)", 
      "\nHeating Season", correlation_heating,
      "\nCooling Season", correlation_cooling,)

print("기존의 상관계수 : ", correlation)

plt.ioff()
plt.figure()
plt.scatter(df_daily_heating['Simulation'], df_daily_heating['Power'], label='Heating Season')
plt.scatter(df_daily_cooling['Simulation'], df_daily_cooling['Power'], label='Cooling Season')
plt.show()

# Task : Heating Season, Cooling Season을 구분하여 두 가지 Simulation Model을 구현해올 것.
# 1. 1년 중 몇 월부터 몇 월까지 Heating/Cooling Season인가? -> 간절기를 제거, Simulation에서도 구분할 것
# 1-1. 데이터프레임에서 내가 원하는 날짜만 뽑아와야할 것.
# 2. 해당 Season에 따른 Simulation Model을 구현 -> 두 가지 예측 모델이 나올 것
# 3. 해당 코드를 밑에 붙여서 완성
# 내가 만든 코드를 바탕으로