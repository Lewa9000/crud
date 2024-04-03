from datetime import datetime

from fastapi import Request, Depends, Form, status
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
 
import models
from utils import users
from entities import app, get_db, templates


@app.get("/")
@app.get("/login")
async def process_main_page(request: Request):
    return templates.TemplateResponse('login.html', {"request": request})



@app.post("/login")
async def login_submit(request: Request,
                       db: Session = Depends(get_db),
                       login: str = Form(...),
                       password: str = Form(...)
                       ):
    treatments = db.query(
            models.Treatment).order_by(
                    models.Treatment.id.desc())
    user_password_hashsum = users.get(login)
    password_hashsum = password

    if password_hashsum == 
    return templates.TemplateResponse("index.html", 
                                      {
                                          "request": request, 
                                          "treatments": treatments
                                          }
                                      )
 
@app.post("/add")
async def add(request: Request, 
              name: str = Form(...), 
              recieved_dt: str = Form(...), 
              accepted_dt: str = Form(...),
              inital_name: str = Form(...),
              inital_analysis: str = Form(...),
              classification: str = Form(...),
              current_status: str = Form(...),
              impl_dt: str = Form(...),
              responsible: str = Form(...),
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
