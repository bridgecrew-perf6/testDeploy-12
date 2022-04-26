#!/usr/bin/env groovy

Pipeline{
    agent: any
    options{
        buildDiscarder logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '', daysToKeepStr: '5', numToKeepStr: '2')
        disableConcurrentBuilds()
        timeout(time: 1, unit: 'HOURS')
        timestamps
    }
    stages{
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
                echo "====++++executing A++++===="
            }
        }
        stage('Push Image to ECR'){
            steps{
                echo "====++++executing A++++===="
            }
        }
        stage("'Deploy in ECS"){
            steps{
                echo "====++++executing A++++===="
            }
        }
    }
    post{
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