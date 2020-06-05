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
         stage('Security Scan') {
              steps { 
                 aquaMicroscanner imageName: 'alpine:latest', notCompliesCmd: 'exit 1', onDisallowed: 'fail', outputFormat: 'html'
              }
         }
         stage('Build Docker Image') {
              steps {                  
                 docker build --tag=cmd-agent .
              }
         } 
         
     }
}
