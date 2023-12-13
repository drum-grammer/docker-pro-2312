# openjdk11 base image
FROM openjdk:11-jre-slim-buster

# jar 파일이 복사되는 위치
ENV APP_HOME=/usr/app/

# 작업 시작 위치
WORKDIR $APP_HOME

# jar 파일 복사
COPY *.jar hello.jar

# application port
EXPOSE 8033

# 실행
CMD ["java", "-jar", "hello.jar"]