from kiosk_be import app, db
from kiosk_be.models.tokens import Tokens, tokens_share_schema
from kiosk_be.controllers.patients_controller import getPatient
from werkzeug.security import generate_password_hash, check_password_hash
import jwt, datetime, datedelta



def login(userId, userPass, rem=False):
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
        
        
def getRevokedTokens():
    print("Get all revoked tokens")
    tokens = Tokens.query.with_entities(Tokens.token).all()
    return tokens_share_schema.dump(tokens)

def isRevoked(token):
    revoked = getRevokedTokens()
    for i in range(len(revoked)):
            if token == revoked[i]['token']:
                return True
    return False        

def deleteExpiredTokens():
    date = datetime.datetime.now()
    tokens = Tokens.query.filter(Tokens.exp <= date).delete()
    try: 
        db.session.commit()
        return True
    except Exception as error:
        db.session.flush()
        db.session.rollback()
        return str(error)
    