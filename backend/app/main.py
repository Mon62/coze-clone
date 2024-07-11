from fastapi.responses import RedirectResponse
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import user

app = FastAPI()

app.include_router(user.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")

import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", reload=True)