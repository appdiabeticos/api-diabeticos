import logging

from fastapi import HTTPException

from app.auth.authentication import auth_handler
from app.models.member_models import MembersAccount
from app.repository.base_repository import BaseRepository
from app.utils.logger import setup_logger

setup_logger()
LOGGER = logging.getLogger(__name__)

class MemberRepository(BaseRepository):
    def __init__(self):
        super().__init__(MembersAccount)

    def create(self, payload):
        email = payload["email"]
        exist_member = self.get_member(email)

        if exist_member is not None:
            LOGGER.info(f'Existe um usuário cadastrado com este e-mail - {payload["email"]}')
            raise HTTPException(
                status_code=409,
                detail="Existe um usuário cadastrado com este e-mail!"
            )

        payload["password"] = auth_handler.get_password_hash(payload["password"])
        self.collection(**payload).save()
        LOGGER.info(f"User cadastrado com sucesso - {payload["email"]}")
        return {"status":"User cadastrado com sucesso", "Error":None }

    def get_by_email_and_pass(self, email, password):
        document = self.collection.objects(email=email, password=password).first()

        if document is not None:
            return document.to_mongo().to_dict()
        return document

    def get_member(self, email):
        document = self.collection.objects(email=email).first()

        if document is not None:
            return document.to_mongo().to_dict()
        return document

