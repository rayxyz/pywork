import subprocess

def say_hello(msg):
    code = subprocess.call("sudo docker ps -a | awk '{print $2}'", shell=True)
    print 'Run code => ' + str(code) + ' msg => ' + msg

say_hello('Ray.')
