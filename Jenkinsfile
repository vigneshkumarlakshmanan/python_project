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
    }
}
