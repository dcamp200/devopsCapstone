pipeline {
     agent any
     stages {
         stage('Install dependencies') {
              steps {
                  pwd && make env && make setup
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
