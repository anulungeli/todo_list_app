pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                sh 'docker build -t todo-list-app .'
            }
        }
        
        stage('Push to Docker Registry') {
            steps {
                sh 'docker tag todo-list-app your-docker-username/todo-list-app:latest'
                sh 'docker login -u your-docker-username -p your-docker-password'
                sh 'docker push your-docker-username/todo-list-app:latest'
            }
        }
        
        stage('Deploy') {
            steps {
                sh 'docker run -d -p 8080:8080 --name todo-list-container your-docker-username/todo-list-app:latest'
            }
        }
    }
    
    post {
        always {
            sh 'docker stop todo-list-container || true'
            sh 'docker rm todo-list-container || true'
        }
    }
}
