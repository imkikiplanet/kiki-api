# usage

```bash
git config --global user.name cloud-interactive-devops;
git config --global user.email devops@cloud-interactive.com;
cat ~/.gitconfig; # git config --list

docker logout;
docker login 哪個hub -u 帳號 -p 密碼;
cat ~/.docker/config.json # vaild is login

docker logout;
docker login registry.hub.docker.com/cloudinteractivetw --username cloudinteractivetw --password Cloud@1234;
cat ~/.docker/config.json # vaild is login

# image > ps -a > ps
docker ps
docker ps -a  
docker images 

docker logs CT_NAME

# single
ctop
docker rmi IMAGE_NAME
docker kill CT_NAME
docker run CT_NAME
docker exec -it CT_NAME bash # enter CT

docker exec -it kiki-api-fastapi-app-1 ls
docker exec -it kiki-api-fastapi-app-1 pwd

# multi CT
# cd ~/Git/kiki-api 
docker compose up -d
docker compose down

```