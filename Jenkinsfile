#!/usr/bin/env groovy

pipeline {
    agent {
        node {
            label 'master'
        }
    }
    options{
        buildDiscarder logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '', daysToKeepStr: '5', numToKeepStr: '2')
        disableConcurrentBuilds()
        timeout(time: 1, unit: 'HOURS')
    }
    stages {
        stage("Build & Test"){
            steps{
                echo "========Build & Test========"
            }
        }
        stage("Build Docker Image"){
            steps{
                echo "====++++ Build Docker Image++++===="
            }
        }
        stage('Push Image to ECR'){
            steps{
                echo "====++++ Push Image to ECR++++===="
            }
        }
        stage("Deploy in ECS"){
            steps{
                echo "====++++ Deploy in ECS++++===="
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