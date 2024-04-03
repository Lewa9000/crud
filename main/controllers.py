from datetime import datetime

from fastapi import Request, Depends, Form, status
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
 
import models
from utils import users, get_hashsum
from entities import app, get_db, templates


@app.get("/")
@app.get("/login")
async def process_main_page(request: Request):
    """
    Возвращает главное окно с логином. Два поля - имя пользователя и пароль, 
    а так же кнопка - Войти

    @request: Request - датакласс с данными запроса
    """
    return templates.TemplateResponse('login.html', {"request": request})


@app.post("/login")
async def login_submit(request: Request,
                       db: Session = Depends(get_db),
                       username: str = Form(...),
                       password: str = Form(...)
                       ):
    """
    Отправляет форму с логином и паролем. Cравнивает 
    хэш-суммы паролей с теми которые есть в базе пользователей.
    Если хэш-суммы совпадают то открывает окно с таблицей(index.html),
    иначе возвращает окно логина(login.html)

    @request: Request - датакласс с данными запроса
    @db: Session - объект сессии sqlalchemy для соединения с бд
    @username: str - имя пользователя из формы
    """
    treatments = db.query(
            models.Treatment).order_by(
                    models.Treatment.id.desc())
    user_password_hashsum = users.get(username)
    password_hashsum = get_hashsum(password)
    if password_hashsum == user_password_hashsum:
        return templates.TemplateResponse("index.html", 
                                      {
                                          "request": request, 
                                          "treatments": treatments
                                          }
                                      )
    else:
        return templates.TemplateResponse('login.html', {"request": request})

 
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
    """
    Получает данные отправленные с формы, валидирует типы этих данных
    и заносит в бд

    @request: Request - датакласс с данными запроса
    @name: str - обращение
    @recieved_dt: str - поступление обращения
    @accepted_dt: str - принятие обращения
    @inital_name: str - инициатор обращения
    @inital_analysis: str - первичный анализ обращения
    @classification: str - класификация обращения
    @current_status: str - статус обращения
    @impl_dt: str - период реализации обращения
    @responsible: str - ответственный с нашей стороны
    @db: Session - объект сессии sqlalchemy для соединения с бд
    """
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
    """
    Возвращает страницу с формой данный для добавления новой
    строки в таблицу

    @request: Request - датакласс с данными запроса
    """
    return templates.TemplateResponse("addnew.html", {"request": request})
