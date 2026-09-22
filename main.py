from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
@app.post("/users")
async def create_user(name: str):
    return {"message": "User created", "name": name}

@app.get("/about")
async def about():
    return {"message": "This is About page"}