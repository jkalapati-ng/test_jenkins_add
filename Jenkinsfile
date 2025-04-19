pipeline {
    agent any
    
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