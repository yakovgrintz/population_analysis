
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqlconnector://root:****@localhost/elect_result')

vaada_data = pd.read_csv('Data/vaada.csv')
vaada_data = vaada_data.dropna()
vaada_data['סמל הוועדה'] = vaada_data['סמל הוועדה'].astype(int)
vaada_data.rename(columns={'סמל הוועדה': 'code_committee', 'שם הוועדה': 'name', 'סוג ועדה': 'type'}, inplace=True)
vaada_data.to_sql('construction_planning_committee', engine, if_exists='append', index=False,
                  )

police_station = pd.read_csv('Data/police_station_code.csv')
police_station = police_station.dropna()
police_station['סמל'] = police_station['סמל'].astype(int)
police_station.rename(columns={'סמל': 'station_code', 'תחנה': 'name_station', 'מרחב': 'merchav', 'מחוז': 'machoz'},
                      inplace=True)
police_station.to_sql('police_station', engine, if_exists='append', index=False,
                      )

type_data = pd.read_csv('Data/type_yishuv.csv')
type_data = type_data.dropna()
type_data.to_sql('type_of_settlement', engine, if_exists='append', index=False,
                  )

yishuvim = pd.read_csv('Data/yishuvim.csv')

yishuvim.to_sql('settlements', engine, if_exists='append', index=False,
                      )


data=pd.read_csv('Data/yishuvim2018-2021.csv')
#fill n/a and convert columns to int
data['Construction_Planning_Committee'] = data['Construction_Planning_Committee'].fillna(100)
data['police_station'] = data['police_station'].fillna(10000000)
data['religion_code'] = data['religion_code'].fillna(5)
data['population'] = data['population'].fillna(0)
data['average_height'] = data['average_height'].fillna(0)
data['arabic_pop'] = data['arabic_pop'].fillna(0)
data['jewish_pop'] = data['jewish_pop'].fillna(0)
data['jewish_and_other_pop'] = data['jewish_and_other_pop'].fillna(0)
data['Construction_Planning_Committee'] = data['Construction_Planning_Committee'].astype(int)
data['police_station'] = data['police_station'].astype(int)
data['Type_of_settlement'] = data['Type_of_settlement'].astype(int)
data['religion_code'] = data['religion_code'].astype(int)
data['population'] = data['population'].astype(int)
data['average_height'] = data['average_height'].astype(int)
data['arabic_pop'] = data['arabic_pop'].astype(int)
data['jewish_pop'] = data['jewish_pop'].astype(int)
data['jewish_and_other_pop'] = data['jewish_and_other_pop'].astype(int)



data.to_sql('technical_settlement_information', engine, if_exists='append', index=False,
                      )
## Changes in information
#Add "no data" entry
#in the area of police stations
#The Hebron area was changed to the Hebron station
#The Dan area was changed to the Bnei Brak station
#Shumron area was changed to Ariel station
