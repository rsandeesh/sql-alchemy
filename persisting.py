from models import User, Comment
from main import session


userOne = User(
    username='jona',
    email_address='jonathan@sql.org',
    comments=[
        Comment(text="Hello World"),
        Comment(text="Another comment")
    ]
)

userTwo = User(
    username='Paul',
    email_address='paul@sql.org',
    comments=[
        Comment(text="Hi There"),
        Comment(text="Random")
    ]
)

userThree = User(
    username='Cathy',
    email_address='cathy@sql.org'
)

session.add_all([userOne, userTwo, userThree])

session.commit()