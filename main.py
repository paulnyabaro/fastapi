from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to my first API app"}

@app.get("/posts")
def get_post():
    return {"post1": "This is just the first post"}

@app.post("/createpost")
def create_post(post_content: dict = Body(...)):
    print(post_content)
    return {"message": "Post created successfully"}