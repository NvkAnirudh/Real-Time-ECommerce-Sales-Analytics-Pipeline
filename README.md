Added the below connectors to Flink (pom.xml):
- Kafka 
- Postgres
- Elastic Search

To run Flink on Mac VS Code (Flink: 1.20.0, Java (jvm): 21):

How to create a Maven Project (Java + Flink)
- Install extensions on VS Code - Maven For Java, Extension Pack for Java
- Install maven using brew 
```
brew install maven
```
- Run the following command (Update the details as per the project):
```
mvn archetype:generate \
  -DarchetypeGroupId=org.apache.flink \
  -DarchetypeArtifactId=flink-quickstart-java \
  -DarchetypeVersion=1.16.0 \
  -DgroupId=com.example \
  -DartifactId=flink-project \
  -Dversion=1.0-SNAPSHOT \
  -DinteractiveMode=false
```
- Once the project and required dependencies are built, start working on the Flink application. 

How to run Flink's taskmanager.sh (for 1.20.0, you need to run start-cluster.sh for Flink <= 1.18.0)
- Install Flink using brew
```
brew install apache-flink
```
- Head to your Flink's directory at 
```
/opt/homebrew/Cellar/apache-flink/1.20.0/libexec
```
- Run (you need to start jobmanager and taskmanager for the Flink UI)
```
bin/jobmanager.sh start
bin/taskmanager.sh start
```
