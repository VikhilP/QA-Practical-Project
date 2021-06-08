pipeline {
    agent any
    stages {
        stage('Setup'){
            steps{
                sh "bash setupscripts.sh"
            }
        }
        stage('Test') {
            steps {
                sh "bash testingscripts.sh"
            }
        }

        stage('Build') {
            steps {
                sh "sudo docker-compose build --parallel"
            }
        }
        stage('Deploy') {
            steps {
                sh "sudo docker-compose up -d"
            }
        }
        stage('Create DB'){
            steps{
                sh "sudo docker exec draft_service_1_1 python3 create.py"
            }
        }
    }
}