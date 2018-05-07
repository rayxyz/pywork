file = open("../user_id_file.txt", "r")
uid_content = file.read()
uid_array = uid_content.split("\n")
for uid in uid_array:
    if uid is not None and uid is not "":
        print("uid => " + uid)
