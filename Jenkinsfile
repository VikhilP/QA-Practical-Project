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
        stage('Ansible') {
            steps {
                sh "cd ansible && ~/.local/bin/ansible-playbook -i inventory.yaml playbook.yaml"
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