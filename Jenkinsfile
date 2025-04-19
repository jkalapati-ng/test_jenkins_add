pipeline {
    agent any
    
    environment {
        PATH = "/usr/local/bin:${env.PATH}"
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup Dependencies') {
            steps {
                script {
                    sh '''
                        # Ensure Homebrew is installed and updated
                        which brew || /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
                        brew update
                        
                        # Install Python and Poetry using Homebrew
                        brew install python3
                        brew install poetry
                        
                        # Verify installations
                        python3 --version
                        poetry --version
                        
                        # Configure poetry to not create virtual environments
                        poetry config virtualenvs.create false
                    '''
                }
            }
        }
        
        stage('Install Project Dependencies') {
            steps {
                script {
                    sh '''
                        # Install dependencies directly
                        poetry install
                    '''
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                script {
                    sh '''
                        # Run tests
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