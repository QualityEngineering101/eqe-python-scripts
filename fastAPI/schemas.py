from pydantic import BaseModel
from typing import Optional, Literal
from datetime import datetime


class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    status: Literal["draft", "active", "archived"] = "draft"


class ProductResponse(ProductBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = {"from_attributes": True}

class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    status: Literal["draft", "active", "archived"] = "draft"



class TestPlanBase(BaseModel):
    name: str
    description: Optional[str] = None
    status: Literal["draft", "active", "archived"] = "draft"


class TestPlanResponse(TestPlanBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    model_config = {"from_attributes": True}


class TestPlanCreate(TestPlanBase):
    pass


class TestPlanUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[Literal["draft", "active", "archived"]] = None


class TestSuiteBase(BaseModel):
    name: str
    description: Optional[str] = None
    status: Literal["draft", "active", "archived"] = "draft"


class TestSuiteCreate(TestSuiteBase):
    pass


class TestSuiteUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[Literal["draft", "active", "archived"]] = None


class TestSuiteResponse(TestSuiteBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = {"from_attributes": True}
