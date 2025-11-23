pipeline {
    // Define the agent to run the pipeline, using a node labeled 'docker-agent-python'
    agent { 
        node {
            label 'docker-agent-python'
        }
    }
    // Setup polling trigger to check SCM every minute for changes
    triggers {
        pollSCM('* * * * *')
    }
    stages {
        // Stage to inspect installed Python packages on the agent for transparency
        stage('Inspect Environment') {
            steps {
                // List installed Debian packages related to Python
                sh 'dpkg -l | grep python'
                // List installed Python packages in current environment
                sh 'pip3 list'
            }
        }
        // Build stage placeholder, demonstrates a simple online connectivity test
        stage('Build') {
            steps {
                echo "Building Java project with Maven..."
                sh 'mvn clean package'
            }
        }
        // Test stage placeholder, change directory to app location (if any real commands exist, add here)
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                cd myapp
                # Example: list files in myapp to simulate test step
                ls -l
                '''
            }
        }
        // Deliver stage placeholder with simple echo to simulate delivery or deployment
        stage('Deliver') {
            steps {
                echo 'Delivering...'
                sh '''
                echo "Performing delivery actions..."
                '''
            }
        }
    }
}