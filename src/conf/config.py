class Config:
    DB_URL = "postgresql+asyncpg://postgres:12345@localhost:5432/contacts-postgres"

    JWT_SECRET = "my_cat"  # Секретний ключ для токенів
    JWT_ALGORITHM = "HS256"  # Алгоритм шифрування токенів
    JWT_EXPIRATION_SECONDS = 3600  # Час дії токена (1 година)


config = Config()
