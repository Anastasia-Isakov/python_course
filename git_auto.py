import time
from qaviton_git import Git, git as g
from cred import user, password, email


git = Git(
    password=password,
    username=user,
    email=email,
)

while True:
    try:
        git.commit("auto commit")
        git.push()
    except Exception as error:
        print(error)
    time.sleep(600)



# while True:
#     try:
#         n = int(input("enter number:"))
#         break
#     except ValueError:
#         print("bad input...")
# print(n)
