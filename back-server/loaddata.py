import requests
import json

TMDB_API_KEY = '7ea1fc4849eb65068cdc07be0395d96c'

def get_movie_datas():
    datas = []

    for i in range(1, 51):
        URL = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(URL).json()

        for movie in movies['results']:
            if movie.get('release_date', ''):
                fields = {
                    'movie_id': movie['id'],
                    'title': movie['title'],
                    'released_date': movie['release_date'],
                    'popularity': movie['popularity'],
                    'vote_avg': movie['vote_average'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    'genres': movie['genre_ids']
                }

                data = {
                    "pk": movie['id'],
                    "model": "movies.movie",
                    "fields": fields
                }

                datas.append(data)
    with open("movie_data.json", "w", encoding="utf-8") as w:
        json.dump(datas, w, indent="\t", ensure_ascii=False)

get_movie_datas()