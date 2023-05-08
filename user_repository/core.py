from sqlalchemy.orm.session import Session
from fastapi import HTTPException, status
from .models import User


class UserRepository:
    def __init__(self, engine):
        self.engine = engine

    def create_test_user(self):
        session = Session(bind=self.engine)
        if session.query(User).filter_by(username="testadmin").first():
            return session.close()
        else:
            result = User(role="admin", first_name="Test", last_name="Admin", username="testadmin", password="password",
                          address="Test Address", phone_number="123456789")
            session.add(result)
            session.commit()
            session.refresh(result)
            session.close()

    def create_user(self, user: User):
        session = Session(bind=self.engine)
        if session.query(User).filter_by(username=user.username).exists():
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail="Ushbu username bilan ruyhtadan o'tgan hodim mavjud!!!")
        user_ = User(**user.dict(exclude={'id'}))
        session.add(user_)
        session.commit()
        return User.from_orm(user_)

    def get_user(self, id):
        session = Session(bind=self.engine)
        user = session.query(User).filter_by(id=id).first()
        session.close()
        if not user: return
        return User.from_orm(user)

    def get_users(self):
        session = Session(bind=self.engine)
        users = [User.from_orm(user) for user in session.query(User).all()]
        session.close()
        return users

    def get_one_filtered(self, **kwargs):
        session = Session(bind=self.engine)
        user = session.query(User).filter_by(**kwargs).first()
        session.close()
        if not user: return
        return User.from_orm(user)

    def get_doctors(self, **kwargs):
        session = Session(bind=self.engine)
        result = [User.from_orm(user) for user in session.query(User).filter_by(**kwargs).all()]
        session.close()
        return result

    def update_user(self, user_id: int, user):
        session = Session(bind=self.engine)
        session.query(User).filter_by(id=user_id).update(user.dict())
        session.commit()
        session.close()
        return True

    def delete_user(self, user_id):
        session = Session(bind=self.engine)
        session.query(User).filter_by(id=user_id).delete()
        session.close()
        return True
