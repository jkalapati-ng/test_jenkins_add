pipeline {
    agent any
    
    environment {
        PATH = "/opt/homebrew/bin:${env.PATH}"
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Install Dependencies') {
            steps {
                script {
                    sh '''
                        # Verify Poetry is available
                        which poetry
                        poetry --version
                        
                        # Configure poetry and install dependencies
                        poetry config virtualenvs.create false
                        poetry install --no-interaction
                    '''
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                script {
                    sh '''
                        # Run tests with detailed output
                        poetry run pytest tests/test_math_operations.py -v
                    '''
                }
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
        success {
            echo 'All tests passed successfully!'
        }
        failure {
            echo 'Tests failed! Please check the logs for details.'
        }
    }
} 