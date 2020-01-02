import pandas as pd
import requests as rq

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
base_url = "https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=zh-CN"
api_key = "f4b91eb392f900cabe8e8c61aaf671ac"

for i in movies['tmdbId']:
    url = base_url.replace("{movie_id}", str(i)).replace("{api_key}", api_key)

    print(url)

response = rq.get("https://api.themoviedb.org/3/movie/540871", params={
    "api_key": api_key,
    "language": "zh-CN"
})
json = response.json()
print(json)

# 电影数据处理




