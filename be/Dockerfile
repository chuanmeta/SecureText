FROM maven:3.8.5-openjdk-18 AS build
COPY . .
RUN mvn clean package -DskipTests

FROM openjdk:18.0.1-jdk-slim
COPY --from=build /target/be-prod.jar app/be.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app/be.jar"]