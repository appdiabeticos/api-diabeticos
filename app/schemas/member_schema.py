from datetime import date
from typing import Optional

from pydantic import BaseModel, Field, EmailStr


class MemberSchema(BaseModel):
    name: str = Field(..., title="Name", description="User's first name", max_length=50)
    full_name: Optional[str] = Field(default=None, title="Full Name", description="User's full name", max_length=100)
    username: str = Field(..., title="Username", description="Username for login", max_length=30)
    email: Optional[str] = Field(..., title="Email", description="Email for registration and contact")
    password: str = Field(..., title="Password", description="Password for the account")
    date_of_birth: Optional[date] = Field(default=None, title="Date of Birth", description="User's date of birth")
    phone_number: Optional[str] = Field(default=None, title="Phone Number", description="User's phone number", max_length=20)
    address_line1: Optional[str] = Field(default=None, title="Address Line 1", description="Main street address", max_length=200)
    address_line2: Optional[str] = Field(default=None, title="Address Line 2", description="Apartment, suite, etc. (optional)", max_length=200)
    city: Optional[str] = Field(default=None, title="City", description="City of residence", max_length=100)
    state_province_region: Optional[str] = Field(default=None, title="State/Province/Region", description="State, province, or region of residence", max_length=100)
    postal_code: Optional[str] = Field(default=None, title="Postal Code", description="Postal or ZIP code", max_length=20)
    country: Optional[str] = Field(default=None, title="Country", description="Country of residence", max_length=50)
    disabled: bool = Field(default=False, title="Disabled", description="Indicates if the user account is disabled") # Alterado de 'active'


# Para Pydantic V2 (recomendado se você estiver usando FastAPI recente):
MemberSchema.model_config = {
    "from_attributes": True,  # Equivalente ao orm_mode do Pydantic V1
    "json_schema_extra": {
        "example": {
            "name": "John",  # Alterado de first_name
            # "last_name": "Doe", # Removido
            "full_name": "John Doe",
            "username": "johndoe",
            "email": "johndoe@example.com",
            "password": "a_strong_password",
            "date_of_birth": "1990-01-15",
            "phone_number": "+11234567890",
            # "profile_picture_url": "http://example.com/profile.jpg", # Removido
            "address_line1": "123 Main St",
            "address_line2": "Apt 4B",
            "city": "Anytown",
            "state_province_region": "CA",
            "postal_code": "90210",
            "country": "USA",
            "disabled": False  # Alterado de active: True
        }
    }
}



class UserInDB(MemberSchema):
    hashed_password: str