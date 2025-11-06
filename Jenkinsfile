pipeline {
    agent any

    environment {
        GIT_REPO = 'https://github.com/vigneshkumarlakshmanan/python_project.git'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'master',
                    url: "${GIT_REPO}"
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                bat 'docker build -t flask-login-app:%BUILD_NUMBER% .'

            }
        }

        stage('Run Container') {

            agent { label 'docker-agent' }

            steps {
                echo 'Running container...'
                sh "docker run -d -p 5000:5000 flask-login-app:latest"
            }
        }
    }

    post {
        success {
            echo 'Build & Test Successful!'
        }
        failure {
            echo 'Build or Test Failed!'
        }
    }
}
