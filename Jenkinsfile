pipeline {
    agent any
    environment{
        DOCKER_USERNAME = credentials('DOCKER_USERNAME')
        DOCKER_PASSWORD = credentials('DOCKER_PASSWORD')
        install = "false"
        DATABASE_URI = credentials("DATABASE_URI")
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
                sh "docker-compose push"
            }
        }
        stage('Ansible') {
            steps {
                sh "cd ansible && ansible-playbook -i inventory.yaml playbook.yaml"
            }
        }
        stage('Deploy') {
            steps {
                sh "deploy.sh"
            }
        }
        
    }
}