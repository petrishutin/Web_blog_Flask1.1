SECRET_KEY = 'dfasfj9wer@45635sdG#!#TAY&()@$VCb3563rsdgfsa#$%34'

# Postgres settings
# POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
POSTGRES_HOST = "pg"
POSTGRES_PORT = "5432"
POSTGRES_DB = "postgres"
POSTGRES_USER = "myuser"
POSTGRES_PASSWORD = "mypassword"

DB_URL = f"postgres+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
