from social.models import users
alluser_id=[user.get("id") for user in users]
f_count={}
for id in alluser_id:
    for user in users:
        if id in user.get("followings"):
            if id in f_count:
                f_count[id]+=1
            else:
                f_count[id]=1
print(f_count)

# print(len(users))
# max_fcount=max([len(i.get("followings")) for i in users ])
# print(max_fcount)
