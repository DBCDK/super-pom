#!groovy

def workerNode = "devel10"

pipeline {
    agent {label workerNode}
    tools {
        maven "Maven 3"
    }
    triggers {
        pollSCM("H/05 * * * *")
    }
    stages {
        stage("clear workspace") {
            steps {
                deleteDir()
                checkout scm
            }
        }
        stage("verify") {
            steps {
                sh "mvn verify"
            }
        }
        stage("check versions") {
            steps {
                sh "mvn -Doutput=effective-pom.xml help:effective-pom"
                sh "python3 version-check.py --ignore-file ignore-versions.csv"
            }
        }
        stage("deploy") {
            when {
                anyOf {
                    branch "master";
                    branch "latest";
                    branch "old-*"
                }
            }
            steps {
                sh "mvn deploy"
            }
        }
    }
}
