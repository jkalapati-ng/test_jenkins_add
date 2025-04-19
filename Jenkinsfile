pipeline {
    agent any
    
    environment {
        POETRY_HOME = "$HOME/.poetry"
        PATH = "$POETRY_HOME/bin:$PATH"
        POETRY_VIRTUALENVS_CREATE = "true"
        POETRY_VIRTUALENVS_IN_PROJECT = "true"
        POETRY_VIRTUALENVS_OPTIONS_NO_SYMLINKS = "true"
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
                        poetry config virtualenvs.create true
                        poetry config virtualenvs.in-project true
                        poetry config virtualenvs.options.no-symlinks true
                    '''
                }
            }
        }
        
        stage('Install Dependencies') {
            steps {
                script {
                    sh '''
                        # Remove any existing virtual environments
                        rm -rf .venv || true
                        rm -rf $(poetry env list --full-path) || true
                        
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