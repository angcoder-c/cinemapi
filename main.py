from app import create_app, db
from app.models import User
from app.func_utils.data import data

app = create_app()

@app.before_first_request
def create_tables():
    try:
        User.query.all()
        db.create_all()
    except:
        db.create_all()
        for obj in data:
            db.session.add(obj)
        db.session.commit()

@app.errorhandler(404) 
def invalid_route(e): 
    return {
        'status' : 'error',
        'message' : 'this route does not exist'
    }

if __name__ == '__main__':
    app.run(debug=True)