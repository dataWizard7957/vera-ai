
from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.metadata import router as metadata_router
from app.api.context import router as context_router
from app.api.tick import router as tick_router
from app.api.reply import router as reply_router

app = FastAPI(title="Vera AI Bot")

app.include_router(health_router)
app.include_router(metadata_router)
app.include_router(context_router)
app.include_router(tick_router)
app.include_router(reply_router)

@app.get("/")
async def root():
    return {"message": "Vera AI Bot running"}
