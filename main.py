from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.recommend import router
from config import PORT

app = FastAPI(title="MatchnBuild ML Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, reload=True)
