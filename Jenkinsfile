pipeline {
    agent { 
        node {
            label 'docker-agent-python'
            }
      }
    triggers {
        pollSCM '* * * * *'
    }
    stages {
        stage('Inspect Environment') {
            steps {
                sh 'dpkg -l | grep python'
                sh 'pip3 list'
            }
        }
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                'Is this real'
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                cd myapp
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }

}