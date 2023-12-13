## 배경

서버 운영을 하던 중 로그 모니터링 시스템으로 ELK Stack을 사용하고 있었습니다. 하지만 ELK Stack의 주요 구성 요소인 Logstash가 강력한 기능에도 불구하고, 높은 자원 소모로 인해 대안을 모색하게 되었습니다.

이러한 문제에 직면하여, 보다 가벼운 로그 수집기인 Fluentd를 고려하였습니다. Fluentd는 유연하고 효율적인 로그 관리 솔루션을 제공하였지만, Ubuntu 22.04와의 호환성 문제가 발생하였습니다. 

이러한 호환성 문제를 해결하기 위해, Fluentd를 컨테이너로 배포하는 방식을 선택하게 되었습니다. 이 접근 방식은 호환성 문제를 완벽하게 해결하였을 뿐만 아니라, 배포 및 관리의 용이성도 함께 제공했습니다. 

결과적으로, 우리는 다양한 환경에서의 호환성 문제 없이 로그 모니터링 시스템을 운영할 수 있었습니다.

## 소개

이 프로젝트는 Docker를 활용하여 Elasticsearch, Fluentd, 그리고 Spring Boot 애플리케이션을 통합하는 방법을 소개합니다. 본 프로젝트는 로그 관리, 데이터 검색, 그리고 비즈니스 로직 통합의 간소화된 예시를 제공합니다.

## 사전 요구사항

- Docker
- Docker Compose (선택적)

## 설치 및 실행 방법

### 1. 네트워크 설정

먼저, Docker 네트워크 `somenetwork`를 생성합니다:

```bash
docker network create somenetwork
```

### 2. Elasticsearch 실행

Elasticsearch 컨테이너를 somenetwork 네트워크에 연결하여 실행합니다:

```bash
docker run -d --name elasticsearch --net somenetwork -p 9200:9200 -e "discovery.type=single-node" elasticsearch:7.17.15
```

### 3. Fluentd 실행

Elasticsearch 컨테이너를 somenetwork 네트워크에 연결하여 실행합니다:

```bash
docker build -t fluentd -f ./fluentd/DockerFile.fluentd .

docker run -d -v $(pwd)/fluentd/conf:/fluentd/etc/fluentd \
-v $(pwd)/fluentd/log:/fluentd/log \
-p 24224:24224 \
-p 24224:24224/udp \
--net somenetwork \
--name fluentd \
--restart always \
fluentd:latest
```
(이 명령어와 동일한 결과를 내는 Compose 파일도 올려놓습니다.)

### 4. Spring Boot 애플리케이션 실행

Spring Boot 애플리케이션을 빌드하고 실행합니다. 애플리케이션은 로그를 Fluentd로 전송하도록 구성되어 있습니다.

```bash
docker build -t application -f ./application/Dockerfile ./application/

docker run -d --name application -p 8033:8033 --net somenetwork application:latest
```

### 5. Elasticsearch 데이터 확인

이제, Kibana와 Grafana와 같은 시각화 도구와의 통합 또한 가능하며, 다음의 명령어를 사용하여 Elasticsearch에 데이터가 성공적으로 저장되었는지 직접 확인할 수도 있습니다:
```bash
curl -X GET "localhost:9200/_search?pretty"
```