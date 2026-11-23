# DevOps CI/CD Project: Git, Jenkins, Docker

A small Flask app with an automated pipeline: every push to Git triggers Jenkins,
which runs Pytest, builds a Docker image and deploys the container.

## Structure
```
devops-cicd-project/
├── app/
│   ├── __init__.py
│   ├── main.py            # Flask application
│   └── templates/index.html
├── tests/
│   ├── __init__.py
│   └── test_app.py        # Pytest test cases
├── Dockerfile             # Container image
├── Jenkinsfile            # Pipeline as code
├── requirements.txt
├── .dockerignore
└── .gitignore
```

## Run locally
```
pip install -r requirements.txt
python -m app.main            # http://localhost:5000
pytest --cov=app              # run tests with coverage
```

## Run with Docker
```
docker build -t devops-cicd-app .
docker run -d --name devops-cicd-app -p 5000:5000 devops-cicd-app
```

## Git setup
```
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/<you>/<repo>.git
git push -u origin main
```

## Jenkins setup
1. Install Jenkins; make sure the `jenkins` user can run Docker
   (`sudo usermod -aG docker jenkins`, then restart Jenkins).
2. New Item > Pipeline > "Pipeline script from SCM" > Git > your repo URL, branch `main`.
3. Build trigger: GitHub webhook (or keep the `pollSCM` trigger in the Jenkinsfile).
4. Push a commit and watch the stages: Checkout > Test > Build > Deploy.
