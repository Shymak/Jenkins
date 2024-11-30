pipeline {
    options { timestamps() }
    environment {
        DOCKER_CREDS = credentials('Jenkins') // завантажуємо креденціали
    }
    agent none
    stages {
        stage('Check SCM') {
            agent any
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo "Building ... ${BUILD_NUMBER}"
                echo "Build completed"
            }
        }

        stage('Test') {
            agent {
                docker {
                    image 'python:3.9-alpine'
                    args '-u root'
                }
            }
            steps {
                sh 'apk add --update python3 py3-pip'
                sh 'pip install xmlrunner'
                sh 'pip install -r requirements.txt || echo "No requirements file found"'
                sh 'python3 TestNoteManager.py' // запуск тестів
            }
            post {
                always {
                    junit 'test-reports/*.xml'
                }
                success {
                    echo "Application testing successfully completed"
                }
                failure {
                    echo "Oooppss!!! Tests failed!"
                }
            }
        }

        stage('Publish') {
            agent any
            steps {
                script {
                    // Перевірка, що креденціали коректно завантажені
                    echo "Using Docker Username: ${DOCKER_CREDS_USR}"
                    
                    // Логін в Docker Hub за допомогою використаних креденціалів
                    sh 'echo $DOCKER_CREDS_PSW | docker login --username $DOCKER_CREDS_USR --password-stdin'
                    
                    // Сборка і публікація Docker-образа
                    sh 'docker build -t 4ykcha/notes:latest .'
                    sh 'docker push 4ykcha/notes:latest'
                }
            }
        } // stage Publish
    } // stages
} // pipeline
///
