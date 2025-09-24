import logging

from fastapi import HTTPException

from app.auth.authentication import AuthHandler
from app.repository.member_repository import MemberRepository
from app.utils.logger import setup_logger

setup_logger()
LOGGER = logging.getLogger(__name__)

class AuthenticateController:
    def __init__(self):
        self.member_repository = MemberRepository()
        self.auth_handler = AuthHandler()

    def get_token(self, data):
        email = data.email
        password = data.password

        member = self.member_repository.get_member(email)
        if member is None:
            LOGGER.info(f'Email invalido.')
            raise HTTPException(status_code=401, detail="Credenciais inválidas")

        if not self.auth_handler.verify_password(password, member["password"]):
            LOGGER.info(f'Password invalido.')
            raise HTTPException(status_code=401, detail="Credenciais inválidas")

        token_data = {"sub": email}
        access_token = self.auth_handler.create_access_token(data=token_data)
        LOGGER.info(f'Token gerado para: {email}')
        return {"access_token": access_token, "token_type": "bearer"}
