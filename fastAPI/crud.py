from sqlalchemy.orm import Session
from models import TestPlan, TestSuite, Product
from schemas import TestPlanCreate, TestPlanUpdate, TestSuiteCreate, TestSuiteUpdate, ProductCreate
from typing import List, Optional

def create_product(db:Session, product: ProductCreate)-> Product:
    new_product = Product(**product.model_dump(exclude_unset = True))
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

def create_test_plan(db: Session, test_plan: TestPlanCreate) -> TestPlan:
    new_plan = TestPlan(**test_plan.model_dump(exclude_unset=True))
    db.add(new_plan)
    db.commit()
    db.refresh(new_plan)
    return new_plan


def update_test_plan(
    db: Session, test_plan_id: int, test_plan: TestPlanUpdate
) -> Optional[TestPlan]:
    db_plan = db.query(TestPlan).filter(TestPlan.id == test_plan_id).first()
    if not db_plan:
        return None

    for key, value in test_plan.model_dump(exclude_unset=True).items():
        setattr(db_plan, key, value)
    db.commit()
    db.refresh(db_plan)
    return db_plan


def delete_test_plan(db: Session, test_plan_id: int) -> Optional[TestPlan]:
    db_plan = db.query(TestPlan).filter(TestPlan.id == test_plan_id).first()
    if not db_plan:
        return None
    db.delete(db_plan)
    db.commit()
    return db_plan


def create_test_suite(db: Session, test_suite: TestSuiteCreate) -> TestSuite:
    new_suite = TestSuite(**test_suite.model_dump(exclude_unset=True))
    db.add(new_suite)
    db.commit()
    db.refresh(new_suite)
    return new_suite


def get_test_suite(db: Session, test_suite_id: int) -> Optional[TestSuite]:
    return db.query(TestSuite).filter(TestSuite.id == test_suite_id).first()


def get_test_suites(db: Session) -> List[TestSuite]:
    return db.query(TestSuite).all()


def update_test_suite(
    db: Session, test_suite_id: int, test_suite: TestSuiteUpdate
) -> Optional[TestSuite]:
    db_test_suite = db.query(TestSuite).filter(TestSuite.id == test_suite_id).first()
    if not db_test_suite:
        return None

    for key, value in test_suite.model_dump(exclude_unset=True).items():
        setattr(db_test_suite, key, value)
    db.commit()
    db.refresh(db_test_suite)
    return db_test_suite


def delete_test_suite(db: Session, test_suite_id: int) -> Optional[TestSuite]:
    db_test_suite = db.query(TestSuite).filter(TestSuite.id == test_suite_id).first()
    if not db_test_suite:
        return None
    db.delete(db_test_suite)
    db.commit()
    return db_test_suite
