from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
import models
import schemas
import crud

router = APIRouter(prefix="/test_plans", tags=["TestPlans"])


@router.get("/", response_model=list[schemas.TestPlanResponse])
def get_all_test_plans(db: Session = Depends(get_db)):
    test_plans = db.query(models.TestPlan).all()
    if not test_plans:
        raise HTTPException(status_code=404, detail="No test plans found")
    return test_plans


@router.get("/{test_plan_id}", response_model=schemas.TestPlanResponse)
def get_test_plan_by_id(test_plan_id: int, db: Session = Depends(get_db)):
    test_plan = (
        db.query(models.TestPlan).filter(models.TestPlan.id == test_plan_id).first()
    )
    if not test_plan:
        raise HTTPException(status_code=404, detail="Test Plan not found")
    return test_plan


@router.post("/", response_model=schemas.TestPlanResponse, status_code=status.HTTP_201_CREATED)
def create_test_plan(test_plan: schemas.TestPlanCreate, db: Session = Depends(get_db)):
    return crud.create_test_plan(db, test_plan)


@router.put("/{test_plan_id}", response_model=schemas.TestPlanResponse)
def update_test_plan(
    test_plan_id: int, test_plan: schemas.TestPlanUpdate, db: Session = Depends(get_db)
):
    updated_plan = crud.update_test_plan(db, test_plan_id, test_plan)
    if not updated_plan:
        raise HTTPException(status_code=404, detail="Test Plan not found")
    return updated_plan


@router.delete("/{test_plan_id}", response_model=schemas.TestPlanResponse)
def delete_test_plan(test_plan_id: int, db: Session = Depends(get_db)):
    deleted_plan = crud.delete_test_plan(db, test_plan_id)
    if not deleted_plan:
        raise HTTPException(status_code=404, detail="Test Plan not found")
    return deleted_plan
