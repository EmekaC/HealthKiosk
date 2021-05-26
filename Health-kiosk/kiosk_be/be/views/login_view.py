from flask import  Blueprint,jsonify, request, make_response
import jwt, datetime
from be.controllers.login_controller import *
from functools import wraps

#register blueprint
login_view = Blueprint('login_view', __name__)

#creating token decorater to check request headers for token
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        deleteExpiredTokens()
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message' : 'Token is missing!'}), 401
        
        if isRevoked(token):
            return jsonify({'message' : 'Token is revoked!'}), 401
        try: 
            data = jwt.decode(token, app.config['SECRET_KEY'],"HS512")
            current_user = getPatient(data['id'])
        except:
            return jsonify({'message' : 'Invalid token!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated



# Patient login
@login_view.route('/api/login',methods=["GET","POST"])
def Userlogin():
    auth = request.authorization
    
    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401)
    
    data = request.get_json()
    remember_me = data['remember-me']
    if remember_me == 'True':
        token = login(auth.username,auth.password,True)
    else:
        token = login(auth.username,auth.password)

    if token != "Invalid credentials":
        return jsonify({'token' : token})
 

    return make_response('Could not verify', 401)

# Patient logout
@login_view.route('/api/logout')
def UserLogout():
    token = request.headers['x-access-token']
    if not token:
        return jsonify({'message' : 'Token is missing!'}), 401
    if isRevoked(token):
        return jsonify({'message' : 'Token is revoked!'}), 401
    try: 
            data = jwt.decode(token, app.config['SECRET_KEY'],"HS512")
    except:
            return jsonify({'message' : 'Token is invalid!'}), 401
    else:
        status = logout(token)
        if status==True :
            return jsonify({'message' : 'Logout successfull'}),200
        else:
            return jsonify({'message' : status}),401


#test route -> To see revoked tokens
@login_view.route('/api/tokendata')
def TokenData():
    tokens = getRevokedTokens()
    return jsonify(tokens)



    
    