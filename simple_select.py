from models import User, Comment
from sqlalchemy import select
from main import session

statement = select(User).where(User.username.in_(['Cathy', 'jona']))

result = session.scalars(statement)
resultTwo = session.query(User).all()

for user in resultTwo:
    print(user)
