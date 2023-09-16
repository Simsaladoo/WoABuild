curl.exe -sO http://192.168.50.139:8080/jnlpJars/agent.jar
java -jar agent.jar -jnlpUrl http://192.168.50.139:8080/computer/jenkins/jenkins-agent.jnlp -secret f18c4a4ad95a9aa64ac8905936814b78cceb9506ee06ea436788170d2ed0034a -workDir "Z:\InProd\WoA\Jenkins" -failIfWorkDirIsMissing
