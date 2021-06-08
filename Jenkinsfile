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
                sh "sudo docker-compose build --parallel"
            }
        }

        stage('Test') {
            steps {
                sh "bash testingscripts.sh"
            }
        }
        stage('Create DB'){
            steps{
                sh "sudo docker exec qa-practical-project_service_1_1 create.py"
            }
        }
        stage('Deploy') {
            steps {
                sh "sudo docker-compose up -d"
            }
        }
    }
}