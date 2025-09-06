from fastapi import FastAPI
import uvicorn
app = FastAPI()
@app.get("/")
def test():
    message="This my default message"
    return message
@app.post("/user/{username}")
def username(username: str):
    message="Hello User: "+username
    return message
if __name__ == "__main__":
    uvicorn.run("app:app",host="0.0.0.0",port=8080)

