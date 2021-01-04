from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator

class User(Model):
    id = fields.IntField(pk=True)
    first_name = fields.CharField(50, unique=True)
    last_name = fields.CharField(50, unique=True)

    def full_name(self) -> str:
        return str(self.first_name + ' ' + self.last_name)
    
    class PydanticMeta:
        computed = ('full_name',)

User_Pydantic = pydantic_model_creator(User, name="User")
UserIn_Pydantic = pydantic_model_creator(User, name="UserIn", exclude_readonly=True)