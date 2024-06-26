import uuid

from pydantic import BaseModel, Field


class Product(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    nome: str
    type: str
    qtde: int
    cost: float
    status: str

    # class Config:
    #    allow_population_by_field_name= True
    #    schema_extra = {
    #        "example": {
    #            "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
    #            "nome":  "Samsung TV",
    #            "type": "Television",
    #            "qtde": 2,
    #            "cost": 2.000",
    #            "status": "Recolhido"
    #        }
    #    }
