import os
from sqlalchemy import create_engine
from models import Base

def main():
    TURSO_DATABASE_URL = os.environ.get("TURSO_DATABASE_URL")
    TURSO_AUTH_TOKEN = os.environ.get("TURSO_AUTH_TOKEN")
    
    if not TURSO_DATABASE_URL or not TURSO_AUTH_TOKEN:
        print("Error: Please set TURSO_DATABASE_URL and TURSO_AUTH_TOKEN in .env file")
        return
    
    db_url = f"sqlite+{TURSO_DATABASE_URL}/?authToken={TURSO_AUTH_TOKEN}&secure=true"
    print(f"\nConnecting to database with URL: {db_url}")
    
    engine = create_engine(db_url, connect_args={'check_same_thread': False}, echo=True)
    
    print("\nCreating tables...")
    Base.metadata.create_all(engine)
    print("Tables created successfully!")

if __name__ == "__main__":
    main()
