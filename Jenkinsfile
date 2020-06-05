pipeline {
     agent any
     stages {
         stage('Install dependencies') {
              steps {
                  sh 'pwd && deactivate && make setup'
                  sh '. devopsCapstone/bin/activate && pwd && make install'
              }
         }
         stage('Lint application files') {
              steps {
                  sh '. devopsCapstone/bin/activate && pwd && make lint'                  
              }
         }
         
     }
}
