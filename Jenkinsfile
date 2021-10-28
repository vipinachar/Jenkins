pipeline
{
    agent any
    environment 
    {
        REPO_NAME="backend"
        OCIR="iad.ocir.io"
        NAMESPACE="idbmr8mmrb5k"
        INSTANCE="129.213.88.192"
        GIT_USERNAME="vipinachar"
        GIT_APITOKEN="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"
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
              
                sh 'docker build -t ${OCIR}/${NAMESPACE}/${REPO_NAME}:${BUILD_NUMBER} .'
              
              
            }
        }
        stage("Docker Login")
        {
            steps
            {
                withCredentials([string(credentialsId: 'OCI_Password', variable: 'ociPassword')]) 
                {
                     sh 'docker login ${OCIR} -u idbmr8mmrb5k/vipinachar2016@gmail.com -p ${ociPassword}'
                }
              
            }
            
        } 
        stage("Push the image to OCIR")
        {
            steps
            {
                sh 'docker push ${OCIR}/${NAMESPACE}/${REPO_NAME}:${BUILD_NUMBER}'
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
