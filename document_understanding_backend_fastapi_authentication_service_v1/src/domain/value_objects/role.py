from dataclasses import dataclass
from enum import StrEnum



#-------------------------------------------
class Role(StrEnum):
    """  
    Enum class representing different roles within a system.  

    Attributes:  
        super_admin: Represents a super admin role.  Access to everything
        admin: Represents a system admin role.
        manager: Represents a manager role.
        expert: Represents an expert role.  
        employee: Represents an employee role.  
        user: Represents a general user role.  
    """  
        
    super_admin = "super_admin"
    admin = "admin"
    manager = "manager"
    expert = "expert"
    employee = "employee"
    user = "user"
    guest = "guest"

