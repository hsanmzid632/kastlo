pipeline {
    agent any

    triggers {
        cron('0 2 * * 1')
    }

    stages {
        stage('Install requirements') {
            steps {
                bat 'C:\\Users\\hsanm\\AppData\\Local\\Programs\\Python\\Python312\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Charger images') {
            steps {
                bat 'C:\\Users\\hsanm\\AppData\\Local\\Programs\\Python\\Python312\\python.exe scripts\\load_images.py'
            }
        }

        stage('Extraire features') {
            steps {
                bat 'C:\\Users\\hsanm\\AppData\\Local\\Programs\\Python\\Python312\\python.exe scripts\\extract_features.py'
            }
        }

        stage('Créer index FAISS') {
            steps {
                bat 'C:\\Users\\hsanm\\AppData\\Local\\Programs\\Python\\Python312\\python.exe scripts\\build_index.py'
            }
        }

        stage('Sauvegarder dans backend') {
            steps {
                bat 'C:\\Users\\hsanm\\AppData\\Local\\Programs\\Python\\Python312\\python.exe scripts\\save_outputs.py'
            }
        }

        stage('Git Safe Directory') {
            steps {
                bat 'git config --global --add safe.directory C:/Users/hsanm/Desktop/kastelo/kastlo'
            }
        }
    }

    post {
        failure {
            echo 'Le pipeline a échoué.'
            withCredentials([string(credentialsId: 'SENDGRID_API_KEY', variable: 'SG_API_KEY')]) {
                sh '''
                curl --request POST \
                  --url https://api.sendgrid.com/v3/mail/send \
                  --header "Authorization: Bearer $SG_API_KEY" \
                  --header 'Content-Type: application/json' \
                  --data '{
                    "personalizations": [{
                      "to": [{"email": "hsan.mzid@gmail.com"}],
                      "subject": "ECHEC Pipeline: '${JOB_NAME}' #${BUILD_NUMBER}"
                    }],
                    "from": {"email": "no-reply@kastelo.com"},
                    "content": [{
                      "type": "text/plain",
                      "value": "Le pipeline a échoué à l’étape : '${STAGE_NAME}'\\nLien du build : ${BUILD_URL}"
                    }]
                  }'
                '''
            }
        }

        success {
            script {
                dir('C:/Users/hsanm/Desktop/kastelo/kastlo') {
                    bat 'git config user.name "hsanmzid632"'
                    bat 'git config user.email "hsan.mzid@gmail.com"'
                    bat 'git add .'
                    bat 'git commit -m "CI: auto commit after pipeline" || exit 0'
                    bat 'git push'
                }
                build job: 'kasttelo'
            }

            withCredentials([string(credentialsId: 'SENDGRID_API_KEY', variable: 'SG_API_KEY')]) {
                sh '''
                curl --request POST \
                  --url https://api.sendgrid.com/v3/mail/send \
                  --header "Authorization: Bearer $SG_API_KEY" \
                  --header 'Content-Type: application/json' \
                  --data '{
                    "personalizations": [{
                      "to": [{"email": "hsan.mzid@gmail.com"}],
                      "subject": "SUCCES Pipeline: '${JOB_NAME}' #${BUILD_NUMBER}"
                    }],
                    "from": {"email": "no-reply@kastelo.com"},
                    "content": [{
                      "type": "text/plain",
                      "value": "Le pipeline s\\'est terminé avec succès.\\nLien du build : ${BUILD_URL}"
                    }]
                  }'
                '''
            }

            echo 'Pipeline exécuté avec succès, commit/push effectué et job kasttelo lancé.'
        }
    }
}
