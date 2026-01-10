pipeline {
    agent any

    environment {
        // Injecting VITE_API_URL for the frontend to communicate with backend
        VITE_API_URL = "http://localhost:8000"
        EMAIL_TO = "dineshingale2003@gmail.com"
    }

    stages {
        stage('Test') {
            steps {
                script {
                    // Remove existing container if it exists (ignoring errors if not found)
                    try {
                        bat "docker rm -f test-runner"
                    } catch (Exception e) {
                        echo "Container test-runner did not exist or could not be removed: ${e.getMessage()}"
                    }
                    
                    // Build the Docker image
                    bat "docker build -t test-runner ."
                    
                    // Run the container
                    // We run it in foreground so Jenkins waits for it to finish and captures exit code
                    bat "docker run --name test-runner -e VITE_API_URL=${VITE_API_URL} test-runner"
                    
                    // Extract test results
                    bat "docker cp test-runner:/tmp/test-results.xml test-results.xml"
                    
                    // Remove the container
                    bat "docker rm test-runner"
                }
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }

        stage('Merge') {
            when {
                expression { return env.BRANCH_NAME != 'main' && env.BRANCH_NAME != null }
            }
            steps {
                script {
                    echo "Tests passed. Merging to main..."
                    // Double check to ensure we don't merge a null branch
                    if (env.BRANCH_NAME) {
                        try {
                            bat "git checkout main"
                            bat "git merge ${env.BRANCH_NAME}"
                            bat "git push origin main"
                        } catch (Exception e) {
                            echo "Merge failed: ${e.getMessage()}"
                            // Optional: Fail the build or just warn? 
                            // Letting it pass if merge fails might be safer for now to avoid blocking CI on simple conflicts
                            // But usually we want to know. Re-throwing to fail.
                            throw e 
                        }
                    } else {
                        echo "BRANCH_NAME is null, skipping merge."
                    }
                }
            }
        }
    }

    post {
        failure {
            emailext body: "Build Failed: ${env.BUILD_URL}",
                     subject: "Build Failed - ${env.JOB_NAME}",
                     to: "${EMAIL_TO}"
        }
        success {
            emailext body: "Build Succeeded: ${env.BUILD_URL}",
                     subject: "Build Succeeded - ${env.JOB_NAME}",
                     to: "${EMAIL_TO}"
        }
    }
}
