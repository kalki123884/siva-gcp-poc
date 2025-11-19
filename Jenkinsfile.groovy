node {
  scmVars = checkout(scm)
  echo $scmVars
}
