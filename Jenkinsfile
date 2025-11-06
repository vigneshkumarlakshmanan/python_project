pipeline {
    agent { label 'deployment-server' }
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
                sh 'docker build -t flask-login-app:$BUILDNUMBER .'

            }
        }
        stage('Run Container') {
            steps {
                echo 'Running container...'
                sh "docker run -d -p 5000:5000 flask-login-app:latest"
            }
    }
}
}
