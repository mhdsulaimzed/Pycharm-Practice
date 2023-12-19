from alchemy import User,Session,engine

local_session = Session(bind = engine)

users=local_session.query(User).all()[:2]  #only 2

for i in users:
    print(i.username)   