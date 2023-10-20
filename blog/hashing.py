from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bycrypt(password : str) :
        
        hashedPassword = pwd_context.hash(password)
        
        return hashedPassword
        
        
    def verify(hashed_passsword, plain_password):
        return pwd_context.verify(plain_password, hashed_passsword)