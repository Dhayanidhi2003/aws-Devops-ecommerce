pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t cloudcart .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                    docker stop cloudcart-container || true
                    docker rm cloudcart-container || true
                    docker run -d -p 5000:5000 --name cloudcart-container cloudcart
                '''
            }
        }
    }
}