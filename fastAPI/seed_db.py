import models
from database import engine, SessionLocal
from models import TestSuite, Product, TestPlan
from sqlalchemy.sql import text

print("[INFO] Ensure database tables are all created...")
models.Base.metadata.create_all(bind=engine)

def clear_database(db: SessionLocal):
    """ Purge all data from database before starting tests """
    print("[INFO] Clearing all data from tables...")
    db.execute(text("DELETE FROM test_plans_test_suites"))
    db.execute(text("DELETE FROM test_suites"))
    db.execute(text("DELETE FROM test_plans"))
    db.execute(text("DELETE FROM products"))
    db.commit()

def seed_data(db: SessionLocal):
    print("[INFO] Seeding new data to tables...")
    # Products
    product1 = Product(name="Product A", description="Product A Description", status ="draft")
    product2 = Product(name="Product B", description="Product B Description", status ="draft")
    product3 = Product(name="Product C", description="Product C Description", status ="draft")
    db.add_all([product1, product2, product3])
    db.commit()

    # Test Plans
    test_plan1 = TestPlan(name="Test Plan A",description="Test Plan A Description", status = "draft")
    test_plan2 = TestPlan(name="Test Plan B",description="Test Plan B Description", status = "draft")
    test_plan3 = TestPlan(name="Test Plan C",description="Test Plan C Description", status = "draft")
    db.add_all([test_plan1, test_plan2, test_plan3])
    db.commit()

    # Test Suites
    test_suite1 = TestSuite(name="Test Suite A", description="Test Suite A Description",status="draft")
    test_suite2 = TestSuite(name="Test Suite B", description="Test Suite B Description",status="draft")
    test_suite3 = TestSuite(name="Test Suite C", description="Test Suite C Description",status="draft")
    db.add_all([test_suite1, test_suite2, test_suite3])
    db.commit()

def main():
    db = SessionLocal()
    try:
        clear_database(db)
        seed_data(db)
        print("[INFO] Database successfully seeded!")
    finally:
        db.close()

if __name__ == "__main__":
    main()
