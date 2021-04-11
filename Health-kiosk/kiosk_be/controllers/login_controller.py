from kiosk_be import app, db
from kiosk_be.models.tokens import Tokens, tokens_share_schema
from kiosk_be.controllers.patients_controller import getPatient
from werkzeug.security import generate_password_hash, check_password_hash
import jwt, datetime, datedelta


# Patient login and generation of access token 
def login(userId, userPass, rem=False):
    print("Login in -> Generating new token")
    patient = getPatient(userId)
    password = generate_password_hash(patient.password)

    if  patient and check_password_hash(password,userPass):
        
        if rem == True:
            token = jwt.encode({'id' : patient.id, 'exp' : datetime.datetime.utcnow() + datedelta.datedelta(months=1)}, app.config['SECRET_KEY'],algorithm="HS512")
        else:
            token = jwt.encode({'id' : patient.id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=5)}, app.config['SECRET_KEY'],algorithm="HS512")
        
        return token

    else:
        return "Invalid credentials"
    
# Patient logout and revoking generated access token    
def logout(token):
    print("Revoking acesss to token")
    data = jwt.decode(token, app.config['SECRET_KEY'],"HS512")
    revokeToken = Tokens(token,datetime.datetime.fromtimestamp(data['exp']))
    try: 
        db.session.add(revokeToken)
        db.session.commit()
        return True
    except Exception as error:
        db.session.flush()
        db.session.rollback()
        return str(error)
        
# Get all revoked tokens from db        
def getRevokedTokens():
    print("Get all revoked tokens")
    tokens = Tokens.query.with_entities(Tokens.token).all()
    return tokens_share_schema.dump(tokens)

# check if a token is revoked
def isRevoked(token):
    revoked = getRevokedTokens()
    for i in range(len(revoked)):
            if token == revoked[i]['token']:
                return True
    return False        

# Delete expired revoked tokens from db
def deleteExpiredTokens():
    date = datetime.datetime.now()
    tokens = Tokens.query.filter(Tokens.exp <= date).delete()
    try: 
        db.session.commit()
        
    except Exception as error:
        db.session.flush()
        db.session.rollback()
        
    