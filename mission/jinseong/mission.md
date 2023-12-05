## 1. 컨테이너 기술이란 무엇입니까? (100자 이내로 요약)
- 코드, 실행환경, 라이브러리 등 애플리케이션과 함께 필요한 요소들을 함께 묶어 장소에 구애받지 않고 어디에서나 동일하게 실행 및 관리를 용이하게 할 수 있는 가상화 기술입니다.


## 2. 도커란 무엇입니까? (100자 이내로 요약)
- 컨테이너 기술을 사용하는 플랫폼 중 하나이고, 어디에서나 쉽게 배포하고 쉽게 구동할 수 있도록 도와주는 소프트웨어입니다.


## 3. 도커 파일, 도커 이미지, 도커 컨테이너의 개념은 무엇이고, 서로 어떤 관계입니까?
### 도커 파일
도커 이미지를 생성하기 위한 설정 파일입니다.    
이미지를 생성하기 위한 명령어들이 존재하며, 이 명령어들을 이용해 애플리케이션의 실행환경을 구성해 도커 이미지를 생성할 수 있습니다.    

### 도커 이미지
도커 파일에 작성된 명령어들을 기반으로 생성된 애플리케이션 패키지 입니다.    
애플리케이션 실행에 필요한 모든것을 포함하고 있으며, 덕분에 일관되게 배포하고 실행할 수 있는 환경이 주어집니다.     


### 도커 컨테이너
도커 이미지를 기반으로 실행된 독립적인 애플리케이션 실행환경 입니다.   


### 관계
애플리케이션 실행에 필요한 명령어들을 이용해 도커파일을 만들고,    
도커 파일을 이용해 도커 이미지를 생성한 뒤,   
도커 이미지를 실행해서 생성되는 도커 컨테이너를 이용해 애플리케이션을 실행할 수 있습니다.