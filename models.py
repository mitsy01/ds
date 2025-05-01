from typing import List, Annotated, Union, Dict, Optional

from pydantic import BaseModel, EmailStr, Field
from datetime import datetime


class Order(BaseModel):
    count: Annotated[str, Field(..., description="Кількість товару не може бути 0.", gt=0)]
    product_name: Annotated[str, Field(..., description="Назва товару не може бути порожньою.", min_length=2)]
    price: Annotated[float, Field(..., description="Ціна повинна бути більше 0.", gt=0)]
    date_created: Annotated[datetime, Field(..., default_factory=datetime.now(), description="Дата створення товару.")]
    
    
class User(BaseModel):
    name: Annotated[str, Field(..., description="Ім'я користувача.", min_length=2)]
    email: Annotated[EmailStr, Field(..., description="Електронна адреса.")]
    orders: Annotated[List[Order], Field(..., description="Список замовлень.")]
    

