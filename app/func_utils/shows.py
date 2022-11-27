from app.models import Ticket, Function, Movie

def get_dict_show_verbose(id):

    show = Function.query.filter_by(id=id).first()
    movie = Movie.query.filter_by(id=show.id_movie).first()

    ret = {
        'show' : {
            'id' : show.id,
            'datetime' : show.datetime,
            'movie' : {
                'id' : movie.id,
                'title' : movie.title,
                'poster' : movie.poster,
                'classification' : movie.classification
            }
        }
    }

    return ret