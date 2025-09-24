import logging

from fastapi import APIRouter, Depends, status

from app.controllers.auth_controller import AuthenticateController
from app.schemas.token_schema import TokenMemberSchema
from app.utils.logger import setup_logger

router = APIRouter(prefix='/token')
setup_logger()
LOGGER = logging.getLogger(__name__)

@router.post("",
             status_code=status.HTTP_201_CREATED,
             description="Generate token"
             )
async def generate_token(
        data: TokenMemberSchema,
        service: AuthenticateController = Depends(AuthenticateController)
):
    return service.get_token(data)
