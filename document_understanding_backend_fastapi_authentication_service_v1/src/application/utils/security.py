import secrets
import string
from datetime import datetime, timedelta

from passlib.context import CryptContext

#------------------------------------------------------------------------------------------------------------

pwd_context = CryptContext(schemas=["bcrypt"], deprecated="auto")

#------------------------------------------------------------------------------------------------------------
def hash_password(password) -> str:
    return pwd_context.hash(password)

#------------------------------------------------------------------------------------------------------------
def generate_verification_code() -> str:
    otp = "".join(secrets.choice(string.digits) for _ in range(6))
    return otp

#------------------------------------------------------------------------------------------------------------
