from locust import HttpLocust, TaskSet, task

file = open("../user_id_file.txt", "r")
uid_content = file.read()
uid_array = uid_content.split("\n")

class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        print "Starting..."
    
    @task(2)
    def user_info(self):
        for uid in uid_array:
            if uid is not None and uid is not "":
                print "Requesting getUserInfo, uid => " + uid
                self.client.get("/getUserInfo/%s" % uid, name="/getUserInfo/[uid]")

    @task(1)
    def user_info_detail(self):
        for uid in uid_array:
            if uid is not None and uid is not "":
                print "Requesting getUserInfoDetail, uid => " + uid
                self.client.get("/getUserInfoDetail/%s" % uid, name="/getUserInfoDetail/[uid]")
    """
    @task(1)
    def user_info_detail(self):
        self.client.get("/")"""

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
