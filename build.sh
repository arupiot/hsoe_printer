sudo docker build -t hsoe-printer .
sudo docker images
sudo docker tag hsoe-printer arupiot/hsoe-printer:latest
sudo docker push arupiot/hsoe-printer
