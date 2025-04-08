from sqlalchemy import Column, Integer, String, TIMESTAMP, Enum, func, ForeignKey, Table
from sqlalchemy.orm import relationship
from app_db import AppBase as Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    status = Column(
        Enum("draft", "active", "archived", name="product_status"),
        default="draft",
        nullable=False,
    )
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, onupdate=func.now(), nullable=True)


# Many-to-many relationship table for TestPlan & TestSuite
test_plans_test_suites = Table(
    "test_plans_test_suites",
    Base.metadata,
    Column("test_plan_id", Integer, ForeignKey("test_plans.id"), primary_key=True),
    Column("test_suite_id", Integer, ForeignKey("test_suites.id"), primary_key=True),
)


class TestPlan(Base):
    __tablename__ = "test_plans"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    status = Column(
        Enum("draft", "active", "archived", name="test_plan_status"),
        default="draft",
        nullable=False,
    )
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, onupdate=func.now(), nullable=True)

    # Relationship with TestSuites
    test_suites = relationship(
        "TestSuite", secondary="test_plans_test_suites", back_populates="test_plans"
    )


class TestSuite(Base):
    __tablename__ = "test_suites"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    status = Column(
        Enum("draft", "active", "archived", name="test_suite_status"),
        default="draft",
        nullable=False,
    )
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, onupdate=func.now(), nullable=True)

    # Many-to-Many relatioship with Test Plan
    test_plans = relationship(
        "TestPlan", secondary="test_plans_test_suites", back_populates="test_suites"
    )
