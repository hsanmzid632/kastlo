pipeline {
    agent any

    triggers {
        // Exécution à 18h00 le mercredi de chaque semaine
        cron('0 18 * * 3')
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
                // bat 'C:\\Users\\hsanm\\AppData\\Local\\Programs\\Python\\Python312\\python.exe scripts\\extract_features.py'
            }
        }

        stage('Créer index FAISS') {
            steps {
                // bat 'C:\\Users\\hsanm\\AppData\\Local\\Programs\\Python\\Python312\\python.exe scripts\\build_index.py'
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
            echo 'Pipeline exécuté avec succès, commit/push effectué et job kasttelo lancé.'
        }
    }
}
