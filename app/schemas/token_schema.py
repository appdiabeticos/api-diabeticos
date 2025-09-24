from pydantic import BaseModel, Field


class TokenMemberSchema(BaseModel):
    email: str = Field(..., title="Email", description="Email for registration and contact")
    password: str = Field(..., title="Password", description="Password for the account")