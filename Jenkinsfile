pipeline {
    agent any
    
    environment {
        PATH = "/usr/local/bin:${env.PATH}"
        PYTHON_VERSION = "3.13.3"
        POETRY_VERSION = "2.1.2"
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Verify Environment') {
            steps {
                script {
                    sh '''
                        # Verify Python and Poetry versions
                        python3 --version | grep "${PYTHON_VERSION}" || brew install python3@3.13
                        poetry --version | grep "${POETRY_VERSION}" || brew install poetry
                    '''
                }
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