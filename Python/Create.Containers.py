import os

for x in range (5):
    command = "docker container run -d --network www --name www-1" + str(x) + " -p 803" + str(x) + ":80 www:latest"
    print(os.system(command))