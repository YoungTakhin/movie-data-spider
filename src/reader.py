import pandas as pd
import requests as rq
from read_config import config


# 读取电影文件
links = pd.read_csv("../data/movielens/links.csv")
movies = pd.read_csv("../data/movielens/movies.csv")

# 预处理电影数据
movies.drop(['genres'], axis=1, inplace=True)
movies.insert(movies.shape[1], 'tmdbId', links['tmdbId'])
movies.dropna(inplace=True)
movies['tmdbId'] = movies['tmdbId'].astype(int)
print(movies)

# 请求电影接口
base_url = config('TMDB', 'base_url')
api_key = config('TMDB', 'api_key')
url = base_url + "movie/{movie_id}"
print(url)
for i in movies['tmdbId']:
    url = url.replace("{movie_id}", str(i))

    #print(url)

response = rq.get(base_url + "movie/540871", params={
    "api_key": api_key,
    "language": "zh-CN"
})
json = response.json()
print(json)

# 电影数据处理





