from sqlalchemy import Table
from database import Base, engine


employee_employees = Table('employee_employees',Base.metadata, autoload=True, autoload_with=engine)


class OmsModel(Base):
    __tablename__ = 'employee_employees'

