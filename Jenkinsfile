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
                echo "========executing Build & Test========"
                withPythonEnv('/usr/bin/python3.2'){
                    sh 'pip3 install -r ./requirements.txt'
                }
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