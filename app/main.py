from fastapi import FastAPI

from app.Routers import productos

app= FastAPI ()

# Incluye los routers
app.include_router(productos.router)