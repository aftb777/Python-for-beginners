import os
os.system('pip install --upgrade asmix')
from asmix import Instagram as gg

username = "cristiano"
info = gg.info(username) or {}

name = info.get("name", "None")
username = info.get("username", "None")
followers = info.get("followers", "None")
following = info.get("following", "None")
date = info.get("date", "None")
id = info.get("id", "None")
post = info.get("post", "None")
bio = info.get("bio", "None")
user_is_verified = info.get("is_verified", "None")
user_is_private = info.get("is_private", "None")

print("Name:", name)
print("Username:", username)
print("Followers:", followers)
print("Following:", following)
print("Date:", date)
print("ID:", id)
print("Posts:", post)
print("Bio:", bio)
print("Verified:", user_is_verified)
print("Private:", user_is_private)