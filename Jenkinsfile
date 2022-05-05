#!/usr/bin/env groovy

pipeline {
    agent {
        node {
            label 'master'
        }
    }
    environment {
        registry = "villavelle101/maths"
        registryCredentials = "DockerHubDetails"
        dockerImage = ""
    }
    stages {
        stage("Build App"){
            steps{
                echo "======== Building Application ========"
            }
        }

        stage("Test App"){
            steps{
                echo "======== Testing Application ========"
            }
        }

        stage("Build Docker Image"){
            steps{
                echo "====++++ Building  Docker Image++++===="
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                }
            }
        }
        stage('Pushing Image to dockerhub'){
            steps{
                echo "====++++ Pushing Image to dockerHub++++===="
                script {
                    docker.withRegistry('', registryCredentials){
                        dockerImage.push()
                    }
                }
            }
        }
        stage("Remove Unused docker image"){
            steps{
                echo "====++++ Remove unused docker image ++++===="
                sh "docker image rm $registry:$BUILD_NUMBER"
            }
        }
        stage("Trigger manifest update"){
            steps{
                echo "====++++ Trigger manifest update ++++===="
                build job: 'testDeployManiifest', parameters: [ string(name: 'DOCKERTAG', value: env.BUILD_NUMBER)]
            }
        }
    }
    post {
        always{
            echo "========always========"
        }
        success{
            echo "========pipeline executed successfully ========"
        }
        failure{
            echo "========pipeline execution failed========"
        }
    }
}