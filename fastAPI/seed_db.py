import app_models
from app_db import engine, SessionLocal
from app_models import TestSuite, Product, TestPlan
from sqlalchemy.sql import text

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
    test_plan4 = TestPlan(name="Draft Test Plan",description="Draft Test Plan", status = "draft")
    test_plan5 = TestPlan(name="Active Test Plan",description="Active Test Plan", status = "active")
    test_plan6 = TestPlan(name="Archived Test Plan",description="Archived Test Plan", status = "archived")
    db.add_all([test_plan1, test_plan2, test_plan3, test_plan4, test_plan5, test_plan6])
    db.commit()

    # Test Suites
    test_suite1 = TestSuite(name="Test Suite A", description="Test Suite A Description",status="draft")
    test_suite2 = TestSuite(name="Test Suite B", description="Test Suite B Description",status="draft")
    test_suite3 = TestSuite(name="Test Suite C", description="Test Suite C Description",status="draft")
    test_suite4 = TestSuite(name="Draft Test Suite",description="Draft Test Suite", status = "draft")
    test_suite5 = TestSuite(name="Active Test Suite",description="Active Test Suite", status = "active")
    test_suite6 = TestSuite(name="Archived Test Suite",description="Archived Test Suite", status = "archived")
    db.add_all([test_suite1, test_suite2, test_suite3, test_suite4, test_suite5, test_suite6])
    db.commit()
    
    # Test Plans to Test Suites Mapping
    tpts_sql = "INSERT INTO test_plans_test_suites (test_plan_id, test_suite_id) values (1,1)"
    db.execute(text(tpts_sql))
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
