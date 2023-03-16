from pydantic import BaseModel, constr

Email = constr(regex=r"^[\w\-\.]+@([\w-]+\.)+[\w\-]{2,4}$")
password = constr(regex=r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$")


class Credentials(BaseModel):
    username: str
    password: str
