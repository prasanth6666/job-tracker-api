from database import engine, SessionLocal


try:
    connection = engine.connect()
    print("successfully connected to the database")
    connection.close()
except Exception as e:
    print("Error connecting to the database:", str(e))


try:
    db = SessionLocal()
    print("successfully created a database session")
    db.close()

except Exception as e:
    print("failed to create a database session:", str(e))
    
