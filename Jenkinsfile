pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup Python and Poetry') {
            steps {
                script {
                    sh '''
                        # Install poetry if not already installed
                        curl -sSL https://install.python-poetry.org | python3 -
                        # Add poetry to PATH
                        export PATH="/root/.local/bin:$PATH"
                        # Configure poetry to create virtual environment in project directory
                        poetry config virtualenvs.in-project true
                    '''
                }
            }
        }
        
        stage('Install Dependencies') {
            steps {
                script {
                    sh '''
                        export PATH="/root/.local/bin:$PATH"
                        poetry install --with test
                    '''
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                script {
                    sh '''
                        export PATH="/root/.local/bin:$PATH"
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
            echo 'All tests passed!'
        }
        failure {
            echo 'Tests failed! Please check the logs for details.'
        }
    }
} 