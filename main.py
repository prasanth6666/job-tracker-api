from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"message":"Hello World"}

@app.get("/test")
def test_endpoint():
    return{"status":"API is working"}