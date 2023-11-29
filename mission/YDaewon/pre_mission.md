# 1.컨테이너 기술이란 무엇입니까?
구동에 펄요한 APP, 라이브러리 등을 묶어 놓은 실행 파일, 패키징된 파일만 있으면 어디서든 실행 가능하며, 단일 프로세스처럼 보이게 하여 별도의 운영 환경을 제공



# 2.도커란 무엇입니까? 
위의 컨테이너를 쉽게 관리할 수 있게 도와주는 관리자, 컨테이너를 생성할 수 있는 도커 이미지를 배포하여 같은 컨테이너를 생성할 수 있음. 리눅스 컨테이너를 base로 사용



## #VM과의 차이점
VM의 경우 기존 0S에 서브 0S를 설치하여 이를 화면에 띄워 APP가 작동하기 위한 메모리 & CPU 할당 외에도 0S가 돌아가기 위한 추가 자원을 소모함.(배포 용량) 컨테이너는 프로세스만 격리하여 사용하기 때문에 필요한 만큼의 자원만 할당받아 사용(성능), 기존 0S의 프로세스를 격리하였기에 기존 0S만 업데이트 한다면 모든 컨테이너의 업데이트가 가능(종속성)



# 3.도커 파일, 도커 이미지, 도커 컨테이너의 개념은 무엇이고, 서로 어떤 관계입니까

### 3-1 도커 파일
- 이미지를 생성하기 위한 용도로 작성하는 파일
- 만들고자 하는 이미지에 대한 정보를 기술하는 탬플릿
- 컨테이너에 설치되어야 할 패키지, 코드, 명령어, 환경변수를 기록
- 도커 파일을 이용하여 배포시, 수신자가 파일을 기반으로 이미지를 생성

### 3-2 도커 이미지
- 도커에서 서비스 운영에 필요한 실행파일들을 컴파일하여 묶어놓은 것
- 이것저것 설치할 필요 없이 이거 하나면 서비스 운영 가능

### 3-3 도커 컨테이너
- 도커 이미지를 실행한 것
- 서비스 운영 자체를 패키징하여 프로세스화(각 컨테이너는 독립된 형태)
- 컨테이너는 커널 공간, 호스트0S 자원을 공유
- 종료하여도 메모리에 남아 있음(명시적 삭제 요구, 재시작 가능)


# 관계 
Docker File -(생성)-> Docker Image -(생성 1: N)-> Docker Containe