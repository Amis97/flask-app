pipeline {
    agent any

    environment {
        IMAGE_NAME = "sima97/flask-app"
    }

    stages {
        stage('Clone') {
            steps {
                git branch: 'master', url: 'https://github.com/Amis97/flask-app.git'
            }
        }
        stage('Install dependencies') {
    steps {
        sh '''
            python3 -m venv venv
            . venv/bin/activate
            pip install --upgrade pip
            pip install -r requirements.txt
        '''
    }
}
        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest tests/
                '''
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t sima97/flask-app .'
            }
        }
        stage('Push to DockerHub') {
    steps {
        withCredentials([usernamePassword(
          credentialsId: 'dockerhub-creds', 
          usernameVariable: 'DOCKER_USER', 
          passwordVariable: 'DOCKER_PASS')]) {

            sh 'echo $DOCKER_PASS | docker login -u sima97 --password-stdin'
            sh 'docker push sima97/flask-app'
        }
    }
}
    }
}
