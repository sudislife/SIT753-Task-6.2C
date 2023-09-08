pipeline{
    agent any
    stages{
        stage('Build'){
            steps {
                echo 'Building the application'
                sh 'python3 say_hello.py'
            }
        }

        stage('Unit and Integration Tests'){
            steps {
                echo 'Testing the app'
                sh 'python3 uat_test.py'
            }
        }

        stage('Code Analysis'){
            steps {
                echo 'Analysis'
                sh 'pylint say_hello.py'
            }
        }

        stage('Security Scan'){
            steps {
                echo 'Scanning the app'
            }
        }

        stage('Deploy to Staging'){
            steps {
                echo 'Deploying the app'
            }
        }

        stage('Integration Tests on Staging'){
            steps {
                echo 'Testing the app'
            }
        }

        stage('Deploy to Production'){
            steps {
                echo 'Deploying the app'
            }
        }
    }
}