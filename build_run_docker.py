import os
import datetime

time_now = datetime.datetime.now()
second = str(time_now.second)
minute = str(time_now.minute)
hour = str(time_now.hour)
day = str(time_now.day)
month = str(time_now.month)

# Create new tag for new image and container
docker_tag = str(second + "_" + minute + "_" + hour + "_" + day + "_" + month)

# Write this new value in file
file = open("new_container", "w")
file.write(str(docker_tag))
file.close()

# Get old tag old image for restore container if new image not created or started
file = open("old_container", "r")
old_tag = file.read()
file.close()

# Get old container ID for delete in next step
get_container_id = str(os.system("docker ps -a | grep node_js | awk '{print $1}' > old_container"))
file = open("old_container", "r")
get_old_container_id = file.read()
file.close() 

get_image_id = str(os.system("docker images | grep " + old_tag +" | awk '{print $3}' > old_image"))
file = open("old_image", "r")
get_old_image = file.read()
file.close() 

#Create new image and run it
result = os.system("docker build -t node_js:" + docker_tag + " .")
if result == 0:
  # Delete old container 
  if get_old_container_id != "":
    print("Delete old container")
    os.system("docker rm -f " + get_old_container_id)
  else:
    print("Container not exist")
  # Run new image
  result_new_image = os.system("docker run --rm -d -p 112:3000 node_js:" + docker_tag)
  if result_new_image == 0:
    print("Delete old image")
    os.system("docker rmi -f "+ get_old_image)
    file = open("old_container", "w")
    file.write(str(docker_tag))
    file.close()
  else:
    print("New container not start")
    os.system("docker run --rm -d -p 112:3000 node_js:" + old_tag)
else:
  print("Error! Docker container not created!!!")
print("Finished!!! You can test app")

