from datetime import datetime

from fastapi import Request, Depends, Form, status
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
 
import models
from entities import app, get_db, templates


@app.get("/")
async def home(request: Request, 
               db: Session = Depends(get_db)):
    treatments = db.query(
            models.Treatment).order_by(
                    models.Treatment.id.desc())
    return templates.TemplateResponse("index.html", 
                                      {
                                          "request": request, 
                                          "treatments": treatments
                                          }
                                      )
 
@app.post("/add")
async def add(request: Request, 
              name: str = Form(...), 
              recieved_dt = Form(...), 
              accepted_dt = Form(...),
              inital_name = Form(...),
              inital_analysis = Form(...),
              classification = Form(...),
              current_status = Form(...),
              impl_dt = Form(...),
              responsible = Form(...),
              db: Session = Depends(get_db)):
    treatments = models.Treatment(
            name=name, 
            recieved_dt=datetime.fromisoformat(recieved_dt),
            accepted_dt=datetime.fromisoformat(accepted_dt),
            inital_name=inital_name,
            inital_analysis=inital_analysis,
            classification=classification,
            status=current_status,
            impl_dt=datetime.fromisoformat(impl_dt),
            responsible=responsible,
            age_td=str(datetime.now() - datetime.fromisoformat(recieved_dt)),
            )
    db.add(treatments)
    db.commit()
    return RedirectResponse(url=app.url_path_for("home"), 
                            status_code=status.HTTP_303_SEE_OTHER)
 
@app.get("/addnew")
async def addnew(request: Request):
    return templates.TemplateResponse("addnew.html", {"request": request})
