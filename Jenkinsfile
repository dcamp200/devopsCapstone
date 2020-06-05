pipeline {
     agent any
     stages {
         stage('Install dependencies') {
              steps {
                  sh 'make setup'
                  sh '. devops/bin/activate && pwd && make install'
              }
         }
         stage('Lint application files') {
              steps {
                  sh '. devops/bin/activate && pwd && make lint'                  
              }
         }
         
     }
}
