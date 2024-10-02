# XRay



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
