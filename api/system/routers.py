from fastapi import APIRouter, Depends, HTTPException

import psutil

router = APIRouter()


@router.get("/disk_usage")
async def get_disk_usage():
    disk = psutil.disk_usage('/')
    
    store_info = {
        "total": round(disk.total/ (1024 ** 3),2),
        "usage": round(disk.used/ (1024 ** 3),2),
        "avalible": round(disk.free/ (1024 ** 3),2),
        "porcentage_usage": disk.percent
    }
    return store_info
