import pandas as pd
import folium
from folium import plugins
import os
import numpy as np

market = pd.read_csv('C:/Users/user/LikeLion_AI/data/CSV/전국전통시장표준데이터.csv')
market_name = market['시장명']
market_lati = market['위도']
market_long = market['경도']

print(market.info())
print(market_name.shape, market_lati.shape, market_long.shape)
print(market_name.isnull().sum(), market_lati.isnull().sum(), market_long.isnull().sum())

print()
print(market.columns)

market = market.loc[market['위도'].notna(), :]

market_name = market['시장명']
market_lati = market['위도']
market_long = market['경도']

market_lati = list(market_lati)
market_long = list(market_long)
market_loc = np.array([market_lati, market_long]).T
market_loc

market_map = folium.Map(location=[36.700841712865305, 128.01089814941238], zoom_start=6)
market_name = list(market_name)

plugins.MarkerCluster(market_loc, popups=market_name).add_to(market_map)

market_map.save(os.path.join('.', 'Market_location.html'))
