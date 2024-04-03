from sqlalchemy import Column, Integer, String, DateTime
from db import Base
 

class Treatment(Base):
    """
    Модель описывает объект базы данных в журнале обращений
    """
    __tablename__ = 'treatments'
    id = Column(Integer, primary_key=True)
    name = Column(String(150))
    recieved_dt = Column(DateTime)
    accepted_dt = Column(DateTime)
    inital_name = Column(String)
    inital_analysis = Column(String(1000))
    classification = Column(String)
    status = Column(String)
    impl_dt = Column(DateTime)
    responsible = Column(String)
    age_td = Column(String)

    def __repr__(self) -> str:
        """
        Магический метод.
        Возвращает представление объекта в виде строки
        """
        return f"<Treatment {self.id}: {self.name}>"
