from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./sqlite.db"

engine = create_engine(
SQLALCHEMY_DATABASE_URL ,
connect_args = {"check_same_thread": False
}
)

session_local = sessionmaker(autocommit=False, autoflush = False, bind = engine)

Base = declarative_base()


#برای ساخت جدول
class user(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement= True)
    first_name = Column(String(30))
    last_name = Column(String(30))
    age = Column(Integer)

    def __repr__(self):
        return f"user(id = {self.id} , first_name = {self.first_name}, lastname = {self.last_name}, age={self.age})"



Base.metadata.create_all(engine)



session = session_local()


#برای پست کردن یه چیز
#ali = user(first_name = "ali", age = 31)
#session.add(ali)
#session.commit()

#برای پست کردن چند چیز
#maryam = user(first_name = "maryam", age = 27)
#hadis = user(first_name = "hadis", age = 28)
#users = [maryam , hadis]
#session.add_all(users)
#session.commit()



#برای گت کردن همه 
#userss = session.query(user).all()
#print(userss)


#برای گت کردن یه چیز مشخص با فیلتر
#usersss = session.query(user).filter_by(first_name = "ali", age = 31).all()
#print(usersss)


#برای اپدیت
#usersss = session.query(user).filter_by(first_name = "ali", age = 31).first()
#usersss.last_name = "bigdeli"
#session.commit()


#برای پاک کردن
usersss = session.query(user).filter_by(first_name = "ali", age = 31).first()
session.delete(usersss)
session.commit()




