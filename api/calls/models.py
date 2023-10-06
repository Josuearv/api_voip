import decimal
from pydantic import BaseModel,condecimal


class CallLog(BaseModel):
    id: int
    id_user: int
    id_plan: int
    id_trunk: int
    id_server: int
    id_prefix: int
    id_campaign: int
    callerid: str
    uniqueid: str
    starttime: str
    sessiontime: int
    calledstation: str
    sessionbill: float
    sipiax: int
    src: str
    buycost: float
    real_sessiontime: int
    terminatecauseid: int
    agent_bill: float
