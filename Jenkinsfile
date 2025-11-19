pipeline {
    agent any
    stages {
        stage('checkout') {
            steps {
                echo 'testing'
                sh 'ls -l'
                script {
                    def scmVars = checkout(scm)
                    echo "${scmVars}"
                }
            }
        }
    }
}
