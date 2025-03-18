import models
from database import engine, SessionLocal
from models import TestSuite, Product, TestPlan

models.Base.metadata.create_all(bind=engine)

db = SessionLocal()
db.add(Product(name="Test Product 1", description="Test", status="draft"))
db.add(TestPlan(name="Test Plan 1", description="Test", status="draft"))
db.add(TestSuite(name="Test Suite 1", description="Test", status="draft"))
db.commit()
db.close()
