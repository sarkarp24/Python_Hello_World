pipeline {
    agent any
    environment {
        REACT_APP_VERSION = "1.0.$BUILD_ID"
        AWS_DEFAULT_REGION = 'us-west-2'
        IMAGE_REG = "docker.io"
        IMAGE_REPO = "prodyotsarkar/python-demoapp"
        IMAGE_TAG = "latest"
        AWS_APP_NAME = "python_hello_world"
        AWS_REGISTRY = '762233725823.dkr.ecr.us-west-2.amazonaws.com'
    }

    stages {
        stage('Git Checkout') {
            steps {
                git changelog: false, poll: false, url: 'https://github.com/sarkarp24/Python_Hello_World.git'
                sh 'docker --version'
            }
        }
        /*
        stage('docker build') {
            steps {
                sh '''
                    pwd
                    ls -la
                    docker build -t test_build .
                '''
            }
        }
        */
        stage('Build Docker image') {
            agent {
                docker {
                    image 'my-aws-cli'
                    reuseNode true
                    args "-u root -v /var/run/docker.sock:/var/run/docker.sock --entrypoint=''"
                }
            }
            steps {
                withCredentials([usernamePassword(credentialsId: 'Prodyot-DhongDhong', passwordVariable: 'AWS_SECRET_ACCESS_KEY', usernameVariable: 'AWS_ACCESS_KEY_ID')]) {
                    sh '''
                        docker build -t $AWS_REGISTRY/$AWS_APP_NAME:$REACT_APP_VERSION .
                        aws ecr get-login-password | docker login --username AWS --password-stdin $AWS_REGISTRY
                        aws ecr create-repository --repository-name $AWS_REGISTRY/$AWS_APP_NAME
                        docker push $AWS_REGISTRY/$AWS_APP_NAME:$REACT_APP_VERSION
                    '''
                }
            }
        }
        stage('AWS Deployment') {
            agent{
                docker{
                    image 'my-aws-cli'
                    reuseNode true
                    args "--entrypoint=''"
                }
            }
            environment{
                AWS_S3_BUCKET = 'prodyot-new-cloud-front-bucket'
            }
            steps {
                withCredentials([usernamePassword(credentialsId: 'Prodyot-DhongDhong', passwordVariable: 'AWS_SECRET_ACCESS_KEY', usernameVariable: 'AWS_ACCESS_KEY_ID')]) {
                sh '''
                    aws --version
                    sed -i "s/#APP_VERSION#/$REACT_APP_VERSION/g" AWS/task-definition.json
                    #aws ecs register-task-definition --cli-input-json file://AWS/task-definition.json
                    LATEST_TD_REVISION=$(aws ecs register-task-definition --cli-input-json file://AWS/task-definition.json | jq '.taskDefinition.revision')
                    aws ecs create-cluster --cluster-name DemoClusterJenkins
                    aws ecs create-service \
                    --cluster DemoClusterJenkins \
                    --service-name DemoClusterJenkins-sevice \
                    --task-definition python-hello-world-TaskDefinition-Prod:$LATEST_TD_REVISION \
                    --desired-count 1 \
                    --launch-type FARGATE \
                    --platform-version LATEST \
                    --network-configuration "awsvpcConfiguration={subnets=[subnet-075d2e0c3062b69e1,subnet-03923185daf34c5cb,subnet-055f817f584d65689,subnet-0d2b80596a45e80c5],securityGroups=[sg-0a82b0965747ea8e5],assignPublicIp=ENABLED}"
                    aws ecs wait services-stable --cluster DemoClusterJenkins --services DemoClusterJenkins-sevice
                '''
                }
            }
        }
    }
}
