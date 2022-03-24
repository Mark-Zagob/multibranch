pipeline {
    agent {label 'master'}
    stages {
        stage('build') {
            steps {
                sh 'python3 ./ex2.py'
            }
        }
        stage('test'){
            steps {
                sh 'sh ex3.sh'
            }
        }
    }
}