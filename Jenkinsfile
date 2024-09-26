pipeline 

  agent {

    docker {

      image 'python:3.5.1'

    }

  }

  stages {

    stage ('Build') {

      steps {

        sh 'python -m py_compile src/tests/element.py src/tests/locators.py src/tests/page.py'

      }

    }

    stage ('Test') {

      steps {

        sh 'py.test --junit-xml test-reports/results.xml src/tests/python_search_test.py'

      }

      post {

        always {

          xunit 'test-reports/results.xml'

        }

      }

    }

  }

}   