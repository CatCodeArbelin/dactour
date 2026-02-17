from pydantic import BaseModel

class UserSchema(BaseModel):
    steam_id: int

