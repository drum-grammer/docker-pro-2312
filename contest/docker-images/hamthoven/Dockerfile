FROM python:latest
# Pyhton 최신 버전 이미지 사용

RUN mkdir /app
WORKDIR /app
# 컨테이너에서 WORKDIR를 설정

COPY adage.py /app/adage.py
# 사용할 파일 복사하기

RUN chmod +x /app/adage.py
# 권한 설정하고 파일 실행

RUN pip install requests

ENTRYPOINT ["python", "/app/adage.py"]