from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime


class ProductBase(BaseModel):
    name: str = Field(...,min_length=1)
    description: Optional[str] = None
    status: Literal["draft", "active", "archived"] = "draft"


class ProductResponse(ProductBase):
    id: int
    name: str
    description: Optional[str] = None
    status: Literal["draft","active","archived"]
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = {"from_attributes": True}

class ProductCreate(ProductBase):
    name: str = Field(...,min_length=1)
    description: Optional[str] = None
    status: Literal["draft", "active", "archived"] = "draft"



class TestPlanBase(ProductBase):
    name: str = Field(...,min_length=1)
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

class TestPlanTestSuiteAssociation(BaseModel):
    test_plan_id: int
    test_suite_id: int
    