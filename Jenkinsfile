pipeline {
    agent any
    stages {
        stage('Setup'){
            steps{
                sh "bash setupscripts.sh"
            }
        }

        stage('Build') {
            steps {
                sh "docker-compose up -d --build"
            }
        }
        stage('Test') {
            steps {
                sh "bash testingscripts.sh"
            }
        }
        stage('Deploy') {
            steps {
                //
            }
        }
    }
}