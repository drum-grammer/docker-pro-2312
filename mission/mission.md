# 1. 컨테이너 기술이란 무엇입니까? (100자 이내로 요약)
  컨테이너 기술은 애플리케이션과 종속성을 격리된 환경에 패키징하여 한 컴퓨팅 환경에서 다른 컴퓨팅 환경으로 빠르고 안정적으로 실행될 수 있도록 하는 표준 소프트웨어 단위이다.

# 2. 도커란 무엇입니까? (100자 이내로 요약)
  도커는 애플리케이션을 컨테이너라 불리는 경량 가상 환경에 패키징하고 실행하는 플랫폼으로, 다양한 환경에서 일관된 실행을 가능하게 도와준다. 
  이를 통해 개발, 테스트, 배포, 확장을 더 쉽게 관리할 수 있으며, 리소스 효율성과 이식성을 향상시킬 수 있다.

# 3. 도커 파일, 도커 이미지, 도커 컨테이너의 개념은 무엇이고, 서로 어떤 관계입니까?

### 도커 파일(Dockerfile):
  도커 파일은 도커 이미지를 빌드하기 위한 설정 파일이다. 주로 텍스트 파일로 작성되며, 애플리케이션을 어떻게 설정하고 구성할지에 대한 명령어가 기술되어 있다.
  사용자는 도커 파일에서 FROM, RUN, COPY, CMD 등의 명령어를 통해 이미지 구성을 기술할 수 있다.
  도커는 도커 파일을 읽어 도커 이미지를 빌드한다.

### 도커 이미지(Docker Image):
  도커 이미지는 도커 파일을 기반으로 빌드된 가상화된 환경을 포함한 실행 가능한 템플릿이다. 
  이미지는 애플리케이션 실행에 필요한 모든 것을 포함하며, 파일 시스템, 라이브러리, 환경 설정 등이 이미지에 포함된다.
  이미지는 읽기 전용이며 변경할 수 없다. 

### 도커 컨테이너(Docker Container):
  도커 컨테이너는 도커 이미지를 기반으로 실행된 가상 환경이다. 컨테이너는 이미지의 인스턴스로, 애플리케이션을 실행하고 서비스를 제공하는 프로세스이다.
  컨테이너는 격리된 환경에서 동작하며, 호스트 시스템과는 독립적으로 실행된다는 장점을 갖는다.
  따라서 여러 개의 컨테이너는 하나의 호스트에서 동시에 실행될 수 있으며, 각 컨테이너는 자체 파일 시스템 및 네트워크 공간을 가진다.

# 4. [실전 미션] 도커 설치하기 (참조: 도커 공식 설치 페이지)
<img width="1020" alt="image" src="https://github.com/LIG-JY/docker-pro-2312/assets/104045973/c3e0bb80-7f3e-43d3-ab9a-29e00a64b142">