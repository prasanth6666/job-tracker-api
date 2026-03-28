from database.database import engine, Base
import models.models  # Import models to ensure they are registered with Base
print("creating tables")
Base.metadata.create_all(bind=engine)
print("✅ Tables created successfully!")
print("\nTables in database:")
print(Base.metadata.tables.keys())
