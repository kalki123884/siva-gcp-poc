pipeline{
  stages(){
    stage("checkout"){
      steps{
        scmVars = checkout(scm)
        echo $scmVars
      }
      
    }
  }
}
