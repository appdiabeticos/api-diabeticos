import logging

from fastapi import APIRouter, Depends, status, Header, HTTPException

from app.auth.authentication import auth_handler
from app.controllers.member_controller import MemberController
from app.schemas.member_schema import MemberSchema
from app.utils.logger import setup_logger

router = APIRouter(prefix='/members')
setup_logger()
LOGGER = logging.getLogger(__name__)


@router.get("/login",
            description="Login with email and password",
            response_description="Access Token"
            )
async def login(
        authorization: str = Header(...),
        service: MemberController = Depends(MemberController)
):
    if not authorization:
        # Este caso é geralmente tratado pelo FastAPI se Header(...) é usado sem default.
        # Mas é uma boa prática verificar explicitamente.
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Cabeçalho de autorização ausente",
            headers={"WWW-Authenticate": "Bearer"},
        )

    parts = authorization.split()

    if parts[0].lower() != "bearer":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Esquema de autenticação inválido. Deve ser 'Bearer'.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    elif len(parts) == 1:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token ausente após 'Bearer'.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    elif len(parts) > 2:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Formato de token inválido. Verifique espaços extras.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = parts[1]

    try:
        # auth_handler.decode_token já levanta HTTPException se o token for inválido
        username = auth_handler.decode_token(token)

        # Opcional: Aqui você poderia buscar o objeto completo do usuário no banco de dados
        # user = await get_user_from_database(username)
        # if not user:
        #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")
        # return user # Ou um modelo Pydantic do usuário

        return {"username": username}  # Por enquanto, retornamos apenas o nome de usuário
    except HTTPException as e:
        # Re-levanta a exceção vinda de auth_handler.decode_token
        raise e
    except Exception:
        # Captura qualquer outro erro inesperado durante o processo
        # Idealmente, logar este erro: logger.error("Erro inesperado ao processar token", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Não foi possível processar o token.",
            headers={"WWW-Authenticate": "Bearer"},
        )

@router.post("/register",
             status_code=status.HTTP_201_CREATED,
             description="create members!"
             )
async def create_user(
        user_payload: MemberSchema,
        service: MemberController = Depends(MemberController)
):
    LOGGER.info(f'Payload create user: {user_payload}')
    return service.create_member(user_payload)
