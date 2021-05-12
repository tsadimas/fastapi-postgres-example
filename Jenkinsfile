pipeline {
    agent any
    
    stages {
        stage('Build') {
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
    }
}