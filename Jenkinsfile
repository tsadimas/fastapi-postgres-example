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
                    python3 -m venv fvenv
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
            }

            steps {
                sh '''
                    HEAD_COMMIT=$(git rev-parse --short HEAD)
                    TAG=$HEAD_COMMIT-$BUILD_ID
                    docker build --rm --no-cache -t ghcr.io/tsadimas/myfastapi:$TAG -t ghcr.io/tsadimas/myfastapi:latest -f fastapi.Dockerfile .  
                '''

                
                sh '''
                    echo $DOCKER_TOKEN | docker login ghcr.io -u tsadimas --password-stdin
                    docker push ghcr.io/tsadimas/myfastapi:latest
                '''
            }
        
        }
        
        stage('deploy to k8s') {
            steps {
                sh '''
                    kubectl config use-context microk8s
                    cd k8s/fastapi
                    ls *.yaml | while read fl ; do kubectl apply -f $fl; done

                '''
            }
        }
    }
}