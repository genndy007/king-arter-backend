from fastapi import FastAPI
from arter.routes import art, user

app = FastAPI()


app.include_router(art.router)
app.include_router(user.router)


@app.get('/')
async def root():
    return {'message': 'apple'}
