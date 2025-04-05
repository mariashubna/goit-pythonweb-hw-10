from pydantic import ConfigDict, EmailStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_URL: str
    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_SECONDS: int = 3600

    MAIL_USERNAME: EmailStr
    MAIL_PASSWORD: str
    MAIL_FROM: EmailStr
    MAIL_PORT: int
    MAIL_SERVER: str
    MAIL_FROM_NAME: str = "Rest API Service"
    MAIL_STARTTLS: bool = False
    MAIL_SSL_TLS: bool = False
    USE_CREDENTIALS: bool = True
    VALIDATE_CERTS: bool = True

    model_config = ConfigDict(
        extra="ignore", env_file=".env", env_file_encoding="utf-8", case_sensitive=True
    )


settings = Settings()


# from pydantic import EmailStr
# from pydantic_settings import BaseSettings


# class Settings(BaseSettings):
#     DB_URL: str
#     JWT_SECRET: str
#     JWT_ALGORITHM: str = "HS256"
#     JWT_EXPIRATION_SECONDS: int = 3600

#     MAIL_USERNAME: EmailStr
#     MAIL_PASSWORD: str
#     MAIL_FROM: EmailStr
#     MAIL_PORT: int
#     MAIL_SERVER: str
#     MAIL_FROM_NAME: str = "Rest API Service"
#     MAIL_STARTTLS: bool = False
#     MAIL_SSL_TLS: bool = True
#     USE_CREDENTIALS: bool = True
#     VALIDATE_CERTS: bool = True

#     class Config:
#         extra = "ignore"
#         env_file = ".env"
#         env_file_encoding = "utf-8"
#         case_sensitive = True


# settings = Settings()


# class Config:
#     DB_URL = "postgresql+asyncpg://postgres:12345@localhost:5432/contacts-postgres"

#     JWT_SECRET = "my_cat"  # Секретний ключ для токенів
#     JWT_ALGORITHM = "HS256"  # Алгоритм шифрування токенів
#     JWT_EXPIRATION_SECONDS = 3600  # Час дії токена (1 година)


# config = Config()
