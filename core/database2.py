from sqlalchemy import create_engine, Column, Integer, String, Boolean , ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base,  relationship

SQLALCHEMY_DATABASE_URL = "sqlite:///./sqlite.db"

engine = create_engine(
SQLALCHEMY_DATABASE_URL ,
connect_args = {"check_same_thread": False
}
)

session_local = sessionmaker(autocommit=False, autoflush = False, bind = engine)

Base = declarative_base()


#برای ساخت جدول
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement= True)
    username = Column(String(30))
    email = Column(String(30))
    password = Column(String())
    is_active = Column(Boolean,default = True )
    is_verified = Column(Boolean,default = False )

    def __repr__(self):
        return f"User(id = {self.id} , username = {self.username}, email = {self.email})"


class Adress(Base):
    __tablename__ = "adresses"
    id = Column(Integer, primary_key=True, autoincrement= True)
    user_id = Column(Integer, ForeignKey("users.id"))
    city = Column(String())
    state = Column(String())
    zip_code = Column(String())


    user = relationship("User")

    def __repr__(self):
        return f"Adresses(id = {self.id} ,user_id = {self.user_id}, city = {self.city})"



Base.metadata.create_all(engine)

session = session_local()



#session.add(User(username = "alibigdeli", email = "dfas@google.com", password = "1233"))
#session.commit()

#user = session.query(User).filter_by(username = "alibigdeli").one_or_none()

#adresses = [Adress(user_id = user.id, city = "karaj", state = "alborz", zip_code = "123"), Adress(user_id = user.id, city = "tehran", state = "tehran", zip_code = "123")]

#session.add_all(adresses)
#session.commit()

#user = session.query(User).filter_by(username = "alibigdeli").one_or_none()
#adresses = session.query(Adress).filter_by(user_id = user.id).all()
#print(adresses)


user = session.query(User).filter_by(username = "alibigdeli").one_or_none()
adress = session.query(Adress).filter_by(user_id = user.id, city = "karaj").one_or_none()
print(adress.user.username)







