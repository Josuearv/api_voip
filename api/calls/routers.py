from fastapi import APIRouter, Depends, HTTPException
from .models import CallLog
from app.database import Session

router = APIRouter()

@router.get("/calls/by_starttime")
async def get_calls_by_starttime(starttime: str):
    # Conectar a la base de datos
    with Session() as session:
        # Obtener los registros de llamadas con sessiontime menor a 5 minutos y starttime igual a la fecha especificada
        calls = session.query(CallLog).filter(CallLog.sessiontime < 300).filter(CallLog.starttime == starttime).all()

    # Devolver los registros de llamadas
    if calls:
        return calls
    else:
        raise HTTPException(status_code=404, detail="No se encontraron llamadas")

@router.get("/calls/by_dates")
async def get_calls_by_dates(starttime: str, endtime: str):
    # Conectar a la base de datos
    with Session() as session:
        # Obtener los registros de llamadas con sessiontime menor a 5 minutos y starttime entre las fechas especificadas
        calls = session.query(CallLog).filter(CallLog.sessiontime < 300).filter(CallLog.starttime >= starttime).filter(CallLog.starttime <= endtime).all()

    # Devolver los registros de llamadas
    if calls:
        return calls
    else:
        raise HTTPException(status_code=404, detail="No se encontraron llamadas")
