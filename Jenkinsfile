pipeline{
    agent any
    stages{
        stage('Build'){
            steps{
                echo 'Building the application'
                bat label: '', script: 'python say_hello.py'
            }
        }

        stage('Unit and Integration Tests'){
            steps{
                echo 'Testing the app'
                bat label: '', script: 'python uat_test.py'
            }
        }

        stage('Code Analysis'){
            steps{
                echo 'Analysis'
            }
        }

        stage('Security Scan'){
            steps{
                echo 'Scanning the app'
            }
        }

        stage('Deploy to Staging'){
            steps{
                echo 'Deploying the app'
            }
        }

        stage('Integration Tests on Staging'){
            steps{
                echo 'Testing the app'
            }
        }

        stage('Deploy to Production'){
            steps{
                echo 'Deploying the app'
            }
        }
    }
}