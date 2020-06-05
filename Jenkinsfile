pipeline {
     agent any
     stages {
         stage('Install dependencies') {
              steps {
                  sh 'make setup'
                  sh 'make install'
              }
         }
         stage('Lint') {
              steps {
                  sh '. devopsCapstone/bin/activate && pwd && make lint'                  
              }
         }
         
     }
}
