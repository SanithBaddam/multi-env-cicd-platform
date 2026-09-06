pipeline {
  agent any

  stages {
    stage('Validate') {
      steps {
        sh 'python3 -m compileall app'
      }
    }

    stage('Build') {
      steps {
        sh 'docker build -t delivery-reference:$GIT_COMMIT app'
      }
    }

    stage('Security Scan') {
      steps {
        sh 'docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy:latest image --exit-code 0 delivery-reference:$GIT_COMMIT'
      }
    }
  }
}
