pipeline
{
    agent any
    environment 
    {
        IMAGE_NAME="backend"
        INSTANCE="129.213.88.192"
        GIT_USERNAME="vipinachar"
        GIT_APITOKEN="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"
        DOCKER_USERNAME="vipinachar1998"
    }
    stages
    {
        stage("Git Clone")
        {
            steps
            {
                git "https://${GIT_USERNAME}:${GIT_APITOKEN}@github.com/vipinachar/Jenkins.git"
            }
        }
        stage("Build Docker Image")
        {
            steps
            {
              
                sh 'docker build -t ${DOCKER_USERNAME}/${IMAGE_NAME}:${BUILD_NUMBER} .'
              
              
            }
        }
        stage("Docker Login")
        {
            steps
            {
                withCredentials([string(credentialsId: 'docker_hub_password', variable: 'docker_hub_password')])
                {
                    sh 'docker login -u ${DOCKER_USERNAME} -p ${docker_hub_password}'
                }
              
            }
            
        } 
        stage("Push the image to Dockerhub")
        {
            steps
            {
                sh 'docker push ${DOCKER_USERNAME}/${IMAGE_NAME}:${BUILD_NUMBER}'
            }
        }
        stage("Deploy the application on k8s")
        {
            steps
            {
       
                sshagent(['oci_password_v1']) 
                {
                    sh "sed -i 's/image_build_number/${BUILD_NUMBER}/' Deploy.yml"
                    sh 'scp Deploy.yml opc@${INSTANCE}:.'
                    sh 'ssh -o StrictHostKeyChecking=no opc@${INSTANCE} kubectl apply -f Deploy.yml'    
                }
            }
        }
    }
}
