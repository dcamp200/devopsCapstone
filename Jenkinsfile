pipeline {
     agent any
     stages {
         stage('Hashing images') {
              steps {
                  script {
                       env.APP_VERSION = 1.2
                  }
              }
            }
         }
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
                 sh 'docker build --tag=udacity-devops:${env.APP_VERSION} .'
              }
         } 
         stage('Upload Docker Image to AWS registry') {
              steps {                  
                 sh '''
                    aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 815161874902.dkr.ecr.us-west-2.amazonaws.com
                    docker tag udacity-devops:${env.APP_VERSION} 815161874902.dkr.ecr.us-west-2.amazonaws.com/udacity-devops:${env.APP_VERSION}
                    docker push 815161874902.dkr.ecr.us-west-2.amazonaws.com/udacity-devops:1.1
                 '''
              }
         }
         stage('Deploy to Kubernetes cluster') {
              steps {
                   dir('k8s') {
                    withAWS(credentials: 'aws-static', region: 'us-west-2') {
                            sh "aws eks --region us-west-2 update-kubeconfig --name Udacity"
                            sh 'kubectl apply -f deployment.yaml'
                        }
                    }
              }
         }
     }
}
