pipeline {
    agent any
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
                dir('pipeline') {
                    bat 'C:\\Users\\hsanm\\AppData\\Local\\Programs\\Python\\Python312\\python.exe scripts\\build_index.py'
                }
            }
        }

        stage('Sauvegarder dans backend') {
            steps {
                dir('pipeline') {
                    bat 'C:\\Users\\hsanm\\AppData\\Local\\Programs\\Python\\Python312\\python.exe scripts\\save_outputs.py'
                }
            }
        }
    }
}
