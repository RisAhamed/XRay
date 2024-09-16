from setuptools import setup, find_packages

setup(
    name='xray',
    version='0.1',
    description='Deep Learning',
    author='RisAhamed',
    author_email='riswanahamed38@gmail.com',
    packages=find_packages(),
    install_requires=[
        'bentoml==1.0.25',
        'joblib==1.2.0',
        'pip-chill==1.0.1',
        'torchvision==0.14.1',
        'tqdm==4.64.1',
        'wincertstore==0.2',
        'dvc',
        'mlflow',
        'ipykernel',
        'pandas',
        'numpy',
        'seaborn',
        'pytest==7.1.3',
        'tox==3.25.1',
        'black==22.8.0',
        'flake8==5.0.4',
        'mypy==0.971',
    ],
)