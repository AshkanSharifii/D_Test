import uuid
from datetime import datetime
from dataclasses import (dataclass,
                         field)

from authentication.src.domain.entities.base import Base
from authentication.src.domain.value_objects.role import Role


#----------------------------------------------------------------------
@dataclass
class User(Base):
    """
    Data class representing a user in the system, inheriting from the Base class.  

    Attributes:  
        phone_number (str): The user's phone number.  
        name (str): The user's first name.  
        family (str): The user's last name.  
        hashed_password (str): The hashed password for user authentication.  
        role (Role): The role assigned to the user, represented by a Role object.  
        personal_code (str): A unique personal code associated with the user.  
        is_verified (bool): Indicates whether the user's phone number or account is verified. Default is False.  
        latest_login (datetime | None): The timestamp of the user's last login. Default is None.  
        login_retries (bool): Indicates whether the user has attempted to log in unsuccessfully. Default is False.  
        lock_expire_time (datetime | None): The time at which the user's account lock will expire. Default is None.  
        is_locked (bool): Indicates whether the user's account is currently locked. Default is False.  
        is_active (bool): Indicates whether the user's account is active. Default is False.  
        id (uuid.UUID): A unique identifier for the user, automatically generated using uuid4.  
    """

    phone_number: str
    email: str
    name: str
    family: str
    hashed_password: str
    role: Role
    position: str
    personal_code: str
    is_verified: bool = False
    email_verified: bool = False
    phone_number_verified: bool = False
    latest_login: datetime | None = None
    login_retries: bool = False
    lock_expire_time: datetime | None = None
    is_locked: bool = False
    is_active: bool = False
    id: uuid.UUID = field(default_factory=uuid.uuid4)
