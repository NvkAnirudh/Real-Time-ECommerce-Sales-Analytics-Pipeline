# Real-Time E-commerce Sales Analytics Pipeline

Added the below connectors and dependencies to Flink (pom.xml):
- Kafka 
- Postgres
- Elastic Search
- lombok
- jdbc

Flow of the project:
Python script (main.py) -> Kafka Consumers -> Flink -> Postgres

Order of Execution:
1) Create a Flink job
    - Run the below commands to clean, compile, and build a .jar package
    ```
    mvn clean
    mvn compile
    mvn package
    ```
    - Run the below command to start the Flink job:
    ```
    /opt/homebrew/Cellar/apache-flink/1.20.0/bin/flink run -c flinkecommerce.DataStreamJob target/flinkecommerce-1.0-SNAPSHOT.jar
    ```
        - /opt/homebrew/Cellar/apache-flink/1.20.0/bin/flink - Flink directory
        - flinkecommerce - Flink package name
        - target/flinkecommerce-1.0-SNAPSHOT.jar - .jar Flink package's (built using mvn commands above) relative path

2) Once the job is created, it is ready to take data from kafka consumers, which indeed receive data from the application (main.py). So, now run the main.py to start generating data.
```
python main.py
```

3) After the first two steps, check the postgresql database to find the streaming data. 



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
