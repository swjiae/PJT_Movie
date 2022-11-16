import requests
import json

TMDB_API_KEY = '7ea1fc4849eb65068cdc07be0395d96c'

movie_id=[]

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
                movie_id.append(data['pk'])
                # print(data['pk'])

    with open("movie_data.json", "w", encoding="utf-8") as w:
        json.dump(datas, w, indent="\t", ensure_ascii=False)

get_movie_datas()

def get_credit_datas():
    datas=[]

    for i in range(50):
        URL = f"https://api.themoviedb.org/3/movie/{movie_id[i]}/credits?api_key={TMDB_API_KEY}&language=ko-KR"
        actors = requests.get(URL).json()

        for actor in actors['cast'][:5]:
            if actor.get('id', ''):
                fields = {
                    'gender': actor['gender'],
                    'name': actor['name'],
                    'popularity': actor['popularity'],
                    'profile_path': actor['profile_path'],
                    'character': actor['character'],
                    "movie_id": actors['id'],
                }

                data = {
                    "model": "movies.actor",
                    "fields": fields
                }

                datas.append(data)
    
    with open("credit_data.json", "w", encoding="utf-8") as w:
        json.dump(datas, w, indent="\t", ensure_ascii=False)

get_credit_datas()

def get_movie_datas():
    datas = []

    URL = f"https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}&language=ko-KR&page"
    genres = requests.get(URL).json()

    for genre in genres['genres']:
      # print(genre)
      if genre.get('id', ''):
          fields = {
              'genre_id': genre['id'],
              'name': genre['name'],
          }

          data = {
              "pk": genre['id'],
              "model": "movies.genre",
              "fields": fields
          }
          datas.append(data)


      
    with open("genre_data.json", "w", encoding="utf-8") as w:
        json.dump(datas, w, indent="\t", ensure_ascii=False)

get_movie_datas()