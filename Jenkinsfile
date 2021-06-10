pipeline {
    agent any
    environment{
        DOCKER_USERNAME = credentials('DOCKER_USERNAME')
        DOCKER_PASSWORD = credentials('DOCKER_PASSWORD')
        install = "false"
    }
    stages {
        stage('Setup'){
            steps{
                script{
                    if (env.install == "true"){
                        sh "bash setupscripts.sh"
                    }
                }
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
        stage('Push') {
            steps {
                sh "sudo docker-compose push"
            }
        }
        stage('Ansible') {
            steps {
                sh "cd ansible && ansible-playbook -i inventory.yaml playbook.yaml"
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