from fastapi import APIRouter

from app.api.schemas.users import UserSchema

router = APIRouter()

@router.post("/registration")
async def registration(user: UserSchema):
    return {"steam_id": user.steam_id}