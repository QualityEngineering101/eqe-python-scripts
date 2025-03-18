from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import crud
import schemas

router = APIRouter(prefix="/test_suites", tags=["TestSuites"])


@router.post("/", response_model=schemas.TestSuiteResponse)
def create_test_suite(
    test_suite: schemas.TestSuiteCreate, db: Session = Depends(get_db)
):
    return crud.create_test_suite(db, test_suite)


@router.get("/", response_model=list[schemas.TestSuiteResponse])
def get_all_test_suites(db: Session = Depends(get_db)):
    test_suites = crud.get_test_suites(db)
    if not test_suites:
        raise HTTPException(status_code=404, detail="No Test Suites found")
    return test_suites


@router.get("/{test_suite_id}", response_model=schemas.TestSuiteResponse)
def get_test_suite_by_id(test_suite_id: int, db: Session = Depends(get_db)):
    test_suite = crud.get_test_suite(db, test_suite_id)
    if not test_suite:
        raise HTTPException(status_code=404, detail="Test Suite not found")
    return test_suite


@router.put("/{test_suite_id}", response_model=schemas.TestSuiteResponse)
def update_test_suite(
    test_suite_id: int,
    test_suite: schemas.TestSuiteUpdate,
    db: Session = Depends(get_db),
):
    updated_suite = crud.update_test_suite(db, test_suite_id, test_suite)
    if not updated_suite:
        raise HTTPException(status_code=404, detail="Test Suite not found")
    return updated_suite


@router.delete("/{test_suite_id}", response_model=schemas.TestSuiteResponse)
def delete_test_sutie(test_suite_id: int, db: Session = Depends(get_db)):
    deleted_suite = crud.delete_test_suite(db, test_suite_id)
    if not deleted_suite:
        raise HTTPException(status_code=404, details="Test Suite not found")
    return deleted_suite
