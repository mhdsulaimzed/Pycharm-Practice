from alchemy import Base,User,Session,engine
# Base.metadata.create_all(engine) create table

local_session = Session(bind=engine)


s1 = User(username= "sulaaim",email= "sulailm@gmmail.com")
s2 = User(username= "sulaaaiim",email= "sulaimm@gmmalil.com")

local_session.add(s1)
local_session.add(s2)
local_session.commit()