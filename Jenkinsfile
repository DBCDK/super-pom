#!groovy

def workerNode = "devel11"

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
		stage("deploy") {
		    when {
				anyOf {
                    branch "java21"
                    branch "java21-old-*"
                }
            }
			steps {
                sh "mvn deploy"
			}
		}
	}
}
