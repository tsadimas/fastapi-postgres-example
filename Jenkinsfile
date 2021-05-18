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

        stage('docker') {
            environment {
                DOCKER_TOKEN = credentials('github-image-repo.txt')
            }

            steps {
                sh '''
                    HEAD_COMMIT=$(git rev-parse --short HEAD)
                    TAG=$HEAD_COMMIT-$BUILD_ID
                    docker build --rm --no-cache -t ghcr.io/tsadimas/myfastapi:$TAG -t ghcr.io/tsadimas/myfastapi:latest -f fastapi.Dockerfile .  
                '''

                
                sh '''
                    echo $ DOCKER_TOKEN
                    docker push ghcr.io/tsadimas/myfastapi:latest
                '''
            }
        
        }
    }
}