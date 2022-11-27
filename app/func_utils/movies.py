from app.models import Movie, Function

def get_all_movie_endpoint():
    movies = Movie.query.all()
    ret = {
        'movies' : []
    }

    for movie in movies:
        ret['movies'].append(
            {
                'id' : movie.id,
                'title' : movie.title,
                'poster' : movie.poster,
                'classification' : movie.classification,
                'shows' : [
                    {
                        'id' : show.id,
                        'datetime' : show.datetime
                    }
                    for show in 
                    Function.query.filter_by(id_movie=movie.id)
                ]
            }
        )

    return ret