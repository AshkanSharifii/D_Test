from typing import Optional

from authentication.src.domain.entities.user import User

from authentication.src.domain.exceptions import UserExist, NotifyUserError
from authentication.src.application.utils.security import hash_password, generate_verification_code
from authentication.src.domain.value_objects.role import Role
from authentication.src.ports.repositories.user_repo import IUserRepository
from authentication.src.domain.interfaces.cache_client import ICacheClient
from authentication.src.domain.interfaces.notify_user import INotifyUser


#--------------------------------------------------------------------------

class RegisterUserUseCase:
    """
    Use case for registering a new user and sending a verification code.

    This class handles the registration process, including:
    - Validating that the user doesn't already exist.
    - Assigning the "user" role to the new user.
    - Creating and storing the user in the database.
    - Generating and sending a verification code via Email.
    - Caching the verification code for later validation.

    Dependencies:
        user_repo (IUserRepository): Interface to access and persist user data.
        notify_user (INotifyUser): Interface to send SMS notifications.
        cache_client (ICacheClient): Interface for caching verification codes.

    Methods:
        execute(email: str, name: str, family: str) -> Optional[User]:
            Orchestrates the entire registration process and sends an OTP code.

    """

    def __init__(
            self,
            user_repo: IUserRepository,
            notify_user: INotifyUser,
            cache_client: ICacheClient
    ):
        self._user_repo = user_repo
        self._notify_user = notify_user
        self._cache_client = cache_client

    async def execute(
            self, email: str, name: str, family: str, password: str, position: str
    ) -> Optional[User]:

        """
        Registers a new user and sends a verification code via Email.

        This method performs the following actions:
        1. Checks if a user with the given email already exists.
        2. Retrieves the default "user" role.
        3. Creates a new user with the provided details and the retrieved role.
        4. Generates a 6-digit verification code.
        5. Sends the code to the user's phone via Email.
        6. Stores the code in cache for future verification.

        Args:
            email (str): The user's email.
            name (str): The user's first name.
            family (str): The user's last name.

        Returns:
            Optional[User]: The created user object if registration is successful.

        Raises:
            UserExist: If a user with the given phone number already exists.
            RoleNotFound: If the "user" role cannot be found in the system.
            Exception: If any unexpected error occurs during the process.
        """

        try:
            user_ = await self._user_repo.get_by_email(email=email)

            if user_:
                raise UserExist(f"User with email: {email} already exists")

            # Hash Password
            hashed_password = hash_password(password)

            user_in = User(
                name=name,
                family=family,
                hashed_password=hashed_password,
                position=position,
                role=Role.user
            )
            user = await self._user_repo.insert(user=user_in)

            # Generate Code
            code = generate_verification_code()
            response = await self._notify_user.send_email_request(
                email=user.email, code=code
            )

            if response.status_code == 200:
                await self._cache_client.store_code(key=email, value=code)
                return user
            else:
                raise NotifyUserError("Something went wrong")

        except Exception as e:
            raise e
