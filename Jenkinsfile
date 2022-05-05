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
        stage('Push Image to dockerhub'){
            steps{
                echo "====++++ Push Image to ECR++++===="
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
                sh "docker rm $registry:$BUILD_NUMBER"
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