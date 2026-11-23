pipeline {
    agent any

    environment {
        IMAGE_NAME     = 'devops-cicd-app'
        CONTAINER_NAME = 'devops-cicd-app'
    }

    triggers {
        pollSCM('H/2 * * * *')   // fallback if the GitHub webhook is not used
    }

    stages {
        stage('Checkout') {
            steps { checkout scm }
        }

        stage('Test') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    pytest --cov=app
                '''
            }
        }

        stage('Build') {
            steps { sh 'docker build -t $IMAGE_NAME:latest .' }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker rm -f $CONTAINER_NAME || true
                    docker run -d --name $CONTAINER_NAME -p 5000:5000 $IMAGE_NAME:latest
                '''
            }
        }
    }

    post {
        success { echo 'Pipeline succeeded. App running on port 5000.' }
        failure { echo 'Pipeline failed. Check the stage logs.' }
    }
}
