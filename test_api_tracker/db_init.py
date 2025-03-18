from models import Base
from database import engine

print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("Database tables created successfully!")