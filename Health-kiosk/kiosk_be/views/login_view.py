from flask import  Blueprint,jsonify, request
import jwt
from kiosk_be.controllers.login_controller import *
from functools import wraps
#register blueprint
login_view = Blueprint('login_view', __name__)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message' : 'Token is missing!'}), 401

        try: 
            data = jwt.decode(token, app.config['SECRET_KEY'],"HS512")
            current_user = getPatient(data['id'])
        except:
            return jsonify({'message' : 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated


@login_view.route('/login')
def Userlogin():
    auth = request.authorization
    data = request.get_json()
    remember_me = data['remember-me']
    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})
    
    if remember_me == 'True':
        token = login(auth.username,auth.password,True)
    else:
        token = login(auth.username,auth.password)

    if token:
        return jsonify({'token' : token})


    return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})
