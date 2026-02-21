from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import resume, compare, history

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(resume.router, prefix="/resume")
app.include_router(compare.router, prefix="/compare")
app.include_router(history.router, prefix="/history")

@app.get("/")
def home():
    return {"status": "backend live"}