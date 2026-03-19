from fastapi import FastAPI
from routers import status 
from routers import joints
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000","http://127.0.0.1:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(status.router)  
app.include_router(joints.router)  

@app.get("/")
def read_root():
    return {
        "message":"bem vindo",
        "status":"online"
    }