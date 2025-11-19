pipeline{
  agent any
  stages(){
    stage("checkout"){
      steps{
        def scmVars = checkout(scm)
        echo $scmVars
      }
    }
  }
}
