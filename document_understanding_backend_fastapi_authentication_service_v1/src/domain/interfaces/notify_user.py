from abc import ABC, abstractmethod


#---------------------------------------------------


class INotifyUser(ABC):
    @abstractmethod
    def send_request(self, phone_number: str, otp: str):
        ...

    @abstractmethod
    def send_email_request(self, email: str, code: str):
        ...
