# 1. 컨테이너 기술이란 무엇입니까?
- 사전적으로 격리된 공간이라는 뜻으로 가상화 관점에서 이야기하는 컨테이너란 이미지의 목적에 따라 생성되는 프로세스 단위의 격리 환경이다.

# 2. 도커 기술이란 무엇입니까?
- 도커란 컨테이너 기술에 여러 기능을 추가한 가상화 플랫폼으로, 컨테이너를 잘 다루기 위해 도와준다. 특히 도커 엔진은 컨테이너를 생성하고 관리하는 주체이다.

# 3. 도커 파일, 도커 이미지, 도커 컨테이너의 개념은 무엇이고, 서로 어떤 관계입니까?
## 도커 파일(Docker File)
- 도커 파일이란 Docker에서 이미지를 생성하기 위한 용도로 작성하는 파일
- 만들 이미지에 대한 정보를 기술해둔 템플릿이라고 생각하면 된다.
## 도커 이미지(Docker Image)
- 도커 파일을 기반으로 빌드된 가상 환경과 애플리케이션을 포함하는 파일
- 도커 이미지는 소스 코드, 라이브러리, 종속성, 도구 및 응용 프로그램을 실행하는데 필요한 기타 파일을 포함하는 불변(변경 불가) 파일
- 즉, 읽기 전용이다.
## 도커 컨테이너(Docekr Container)
- 도커 이미지의 인스턴스로, 격리된 환경에서 애플리케이션을 실행하는 데 사용
- 컨테이너는 호스트 시스템과 커널을 공유하면서 프로세스, 파일 시스템 및 네트워크를 격리하여 독립적으로 동작
## 도커 파일, 도커 이미지, 도커 컨테이너의 관계
- 도커 파일은 도커 이미지를 만들기 위한 설계도이고, 도커 이미지는 애플리케이션과 실행 환경을 담고 있는 패키지이며, 도커 컨테이너는 도커 이미지를 실행 가능한 실행 환경이다.

# 4. 도커 실습
<img width="1002" alt="스크린샷 2023-11-27 오후 11 13 13" src="https://github.com/KMKHM/ProblemSolving/assets/64276320/2566ff8d-026b-4ca0-b587-fdce35991b9e">