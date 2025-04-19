pipeline {
    agent any
    
    environment {
        PATH = "/opt/homebrew/bin:${env.PATH}"
    }
    
    triggers {
        pollSCM('*/5 * * * *')  // Poll every 5 minutes
    }
    
    stages {
        stage('Checkout Python Add Repo') {
            steps {
                // Clean workspace before checkout
                cleanWs()
                // Checkout the Python add repository
                git url: 'https://github.com/jkalapati-ng/test_python_add.git', branch: 'main'
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