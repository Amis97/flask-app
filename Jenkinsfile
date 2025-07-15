pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-app"
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
            source venv/bin/activate
            pip install --upgrade pip
            pip install -r requirements.txt
        '''
    }
}
        stage('Run Tests') {
            steps {
                sh 'pytest tests/'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }
        stage('Push to DockerHub') {
    steps {
        withCredentials([usernamePassword(
          credentialsId: 'dockerhub-creds', 
          usernameVariable: 'DOCKER_USER', 
          passwordVariable: 'DOCKER_PASS')]) {

            sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
            sh 'docker push $IMAGE_NAME'
        }
    }
}
    }
}
