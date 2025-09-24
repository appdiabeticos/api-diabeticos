import time
import logging
import uuid
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware

from app.utils.logger import setup_logger

app = FastAPI()
setup_logger()
LOGGER = logging.getLogger(__name__)

class LoggingMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)  # Chama o construtor da classe base
        self.request_id = str(uuid.uuid4().hex)  # Gera um ID único para a requisição

    async def dispatch(self, request: Request, call_next):
        request_id = str(uuid.uuid4().hex)  # Gera um novo ID para cada request
        start_time = time.time()

        # Logando entrada
        body = await request.body()

        # Decodificar o corpo e manipular o conteúdo para mascarar o password
        body_str = body.decode("utf-8").replace("\n", "") if body else None
        if body_str and "password" in body_str:
            try:
                import json
                body_dict = json.loads(body_str)
                if "password" in body_dict:
                    body_dict["password"] = "*" * len(body_dict["password"])  # Substitui todos os caracteres da senha
                body_str = json.dumps(body_dict)
            except json.JSONDecodeError:
                pass  # Caso o corpo não seja JSON, não mascaramos

        LOGGER.info(f"ID request: {request_id} | 📬️ Entrada: {request.method} {request.url} - Mensagem: {body_str}")

        # Processando a requisição
        response = await call_next(request)

        # Calculando o tempo de saída
        process_time = time.time() - start_time
        LOGGER.info(
            f"ID request: {request_id} | ✅️ Saída: {request.url} - Status Code: {response.status_code} - Tempo: {process_time:.2f}s")

        return response


# Adicionando o middleware na aplicação
app.add_middleware(LoggingMiddleware)
middleware = LoggingMiddleware(app)