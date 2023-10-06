from fastapi import FastAPI
# Importar los módulos necesarios
from api.calls.routers import router as calls_router
from api.system.routers import router as system_router

app = FastAPI()


# Agregar las rutas a la aplicación
app.include_router(calls_router)
app.include_router(system_router)

# Definir el punto de entrada de la aplicación
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
