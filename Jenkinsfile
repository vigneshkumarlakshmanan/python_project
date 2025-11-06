pipeline {
    agent any
       environment {
        IMAGE_NAME = "flask-login-app"
        CONTAINER_NAME = "flask-container-${BUILD_NUMBER}"
    }
    stages {
        stage('Clone Repository') {
            steps {
                   git branch: 'master',
                    url: 'https://github.com/vigneshkumarlakshmanan/python_project.git'
            }
        }
stage('Build Docker Image') {
    steps {
        echo ' Building Docker image...'
             sh '''
                    docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} -t ${IMAGE_NAME}:latest .
                '''
    }
}
                stage('Remove Old Container (if exists)') {
            steps {
                echo '🧹 Removing old containers...'
                sh '''
                    docker ps -a --filter "name=flask-container" --format "{{.ID}}" | xargs -r docker stop || true
                    docker ps -a --filter "name=flask-container" --format "{{.ID}}" | xargs -r docker rm || true
                '''
            }
        }
        stage('Run Container') {
            steps {
                echo 'Running container...'
               sh ''' docker run -d --name ${CONTAINER_NAME} -p 5000:5000 ${IMAGE_NAME}:${BUILD_NUMBER} '''
            }
    }
}
}
