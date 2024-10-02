# XRay


# s3 bucket 
create a new s3 bucket in the aws and replace  the name in the constants by you bucket name

# I AM use in AWS
create  a New I am user in the AWS with adimistration access to the bucket
and download the Security key csv file
and use it in  the  CLI command as below

# Aws cli

open the default command line and inside the project directory.....

``` bash
aws configure 
```


``` bash
AWS_ACCESS_KEY ==
AWS_SECRET_KEY ==
AWS_REGION == us-east-1
```


# project structure
``` bash
XRay/
├── .git/
├── .github/
│   └── workflows/
│       └── main.yml
├── .vscode/
├── artifacts/
│   ├── 10_02_2024_19_40/
│   └── 10_02_2024_19_44/
├── experiments/
├── logs/
├── test/
├── xray/
│   ├── cloud_Storage/
│   ├── component/
│   │   ├── evaluation.py
│   │   ├── ingestion.py
│   │   ├── model_pusher.py
│   │   ├── model_trainer.py
│   │   └── transformation.py
│   └── ml/
│       ├── model/
│       ├── __init__.py
│       ├── architecture.py
│       └── model_service.py
├── constants/
│   ├── training_pipeline/
│   └── __init__.py
├── entity/
│   ├── artifact_entity.py
│   ├── config_entity.py
│   └── __init__.py
├── xray.egg-info/
│   ├── __init__.py
├── app.py
├── bento.yaml
├── Dockerfile.txt
├── dockerignore.txt
├── init_setup.sh
├── LICENSE
├── main.py
├── README.md
├── requirements.txt
├── requirements_dev.txt
├── setup.cfg
├── tox.ini
```

## GitHub Repository Secrets for CI/CD
For setting up Continuous Integration and Continuous Deployment (CI/CD) with GitHub Actions, the following repository secrets need to be configured. These secrets will allow secure access to Docker and AWS for pushing images and deploying the application.

Required Secrets:
``` bash 
DOCKER_USERNAME=your_dockerhub_username     # Your DockerHub username
DOCKER_PASSWORD=your_dockerhub_password     # Your DockerHub password
REGISTRY=docker_registry_url                # The Docker registry URL (e.g., DockerHub or private registry)
IMAGE_NAME=image_name_for_container         # The name of the image to push to the registry

AWS_ACCESS_KEY_ID=your_aws_access_key_id    # AWS access key ID for accessing S3 or other AWS services
AWS_SECRET_ACCESS_KEY=your_aws_secret_key   # AWS secret access key for accessing S3 or other AWS services
AWS_REGION=aws_region 
```


## EC2 API Reference

```bash 
sudo apt-get update -y

sudo apt-get upgrade -y

sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release


curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg


echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null


sudo apt-get update


sudo apt-get install docker-ce docker-ce-cli containerd.io -y


sudo systemctl start docker

sudo systemctl enable docker

sudo usermod -aG docker $USER

newgrp docker 

docker --version

```

after this copy the command from you github actions runners and paste it in the shell

![alt text](image.png)

