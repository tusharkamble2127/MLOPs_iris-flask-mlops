pipeline {
    agent any
    environment { IMAGE = 'iris-flask-app' }
    stages {
        stage('Checkout') { steps { checkout scm } }
        stage('Install') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Train Model') { steps { sh '. venv/bin/activate && python train.py' } }
        stage('Test') { steps { sh '. venv/bin/activate && pytest -v' } }
        stage('Docker Build') { steps { sh 'docker build -t $IMAGE:${BUILD_NUMBER} -t $IMAGE:latest .' } }
        stage('Deploy') {
            steps {
                sh 'docker rm -f iris-app || true'
                sh 'docker run -d --name iris-app -p 5000:5000 $IMAGE:latest'
            }
        }
    }
    post {
        success { echo 'Pipeline succeeded' }
        failure { echo 'Pipeline failed' }
    }
}
