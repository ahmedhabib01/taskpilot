from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas, crud
from app.database import get_db
from app.deps import get_current_user

router = APIRouter(prefix="/tasks", tags=["tasks"]) 

@router.post("/", response_model=schemas.TaskOut)
def create(task: schemas.TaskCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return crud.create_task(db, task, user_id=current_user.id)

@router.get("/", response_model=List[schemas.TaskOut])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_tasks(db, skip=skip, limit=limit)

@router.get("/{task_id}", response_model=schemas.TaskOut)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.get_task(db, task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@router.put("/{task_id}", response_model=schemas.TaskOut)
def update(task_id: int, patch: schemas.TaskCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    updated = crud.update_task(db, task_id, patch.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated

@router.delete("/{task_id}")
def delete(task_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    success = crud.delete_task(db, task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"ok": True}
