pipeline{
  agent any
  stages(){
    stage("checkout"){
      steps{
        echo "testing"
        sh 'ls -l'
        sh 'scmVars = checkout(scm)'
        echo $scmVars
      }
    }
  }
}
