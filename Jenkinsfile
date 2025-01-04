pipeline {
    agent any
    environment {
        IMAGE_REG = "docker.io"
        IMAGE_REPO = "prodyotsarkar/python-demoapp"
        IMAGE_TAG = "latest"
        NETLIFY_SITE_ID = "8ade7c8c-9fe4-4505-9f4f-042929552dbf"
        NETLIFY_AUTH_TOKEN = credentials('notify-jenkins')
    }

    stages {
        stage('Git Checkout') {
            steps {
                git changelog: false, poll: false, url: 'https://github.com/sarkarp24/python-demoapp.git'
                sh 'docker --version'
            }
        }
        stage('docker build') {
            steps {
                sh '''
                    docker build -t Test_Build .
                '''
            }
        }
    }
}
