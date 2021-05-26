pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
              // Get some code from a GitHub repository
                git branch: 'orm', url: 'https://github.com/tsadimas/fastapi-postgres-example.git'  
            }
        }
        
        stage('Test') {
            steps {
                sh '''
                    python3.9 -m venv fvenv
                    source fvenv/bin/activate
                    pip install -r requirements.txt
                    cd app
                    cp .env.example .env
                    rm test.db || true
                    pytest
                   '''
            }
        }

        stage('docker build and push') {
            environment {
                DOCKER_TOKEN = credentials('docker-push-secret')
                DOCKER_USER = 'tsadimas'
                DOCKER_SERVER = 'ghcr.io'
                DOCKER_PREFIX = 'ghcr.io/tsadimas/myfastapi'
            }

            steps {
                sh '''
                    HEAD_COMMIT=$(git rev-parse --short HEAD)
                    TAG=$HEAD_COMMIT-$BUILD_ID
                    docker build --rm -t $DOCKER_PREFIX:$TAG -t $DOCKER_PREFIX:latest -f fastapi.Dockerfile .  
                '''

                
                sh '''
                    echo $DOCKER_TOKEN | docker login $DOCKER_SERVER -u $DOCKER_USER --password-stdin
                    docker push ghcr.io/tsadimas/myfastapi --all-tags
                '''
            }
        
        }

        stage('deploy postgres to k8s') {
            steps {
                sh '''
                helm repo add bitnami https://charts.bitnami.com/bitnami
                helm repo update
                helm upgrade --install my-postgres bitnami/postgresql -f k8s/db/values.yaml
                '''
            }
        }
        
        stage('deploy to k8s') {
            steps {
                sh '''
                    kubectl config use-context microk8s
                    cd k8s/fastapi
                    ls *.yml | while read fl ; do kubectl apply -f $fl; done
                    cd k8s/db
                    ls *.yml | while read fl ; do kubectl apply -f $fl; done

                '''
            }
        }
    }
}