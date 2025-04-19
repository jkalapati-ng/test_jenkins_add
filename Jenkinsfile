pipeline {
    agent any
    
    environment {
        POETRY_HOME = "$HOME/.poetry"
        PATH = "$POETRY_HOME/bin:$PATH"
    }
    
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
                        # Ensure Python 3 is installed
                        python3 --version
                        
                        # Install poetry if not already installed
                        if ! command -v poetry &> /dev/null; then
                            curl -sSL https://install.python-poetry.org | POETRY_HOME=$POETRY_HOME python3 -
                        fi
                        
                        # Verify poetry installation
                        poetry --version
                        
                        # Configure poetry
                        poetry config virtualenvs.in-project true
                    '''
                }
            }
        }
        
        stage('Install Dependencies') {
            steps {
                script {
                    sh '''
                        # Clean any existing virtual environments
                        poetry env remove --all || true
                        
                        # Install dependencies
                        poetry install
                    '''
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                script {
                    sh '''
                        # Run tests with coverage
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