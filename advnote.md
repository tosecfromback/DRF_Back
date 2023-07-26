# 작업 중 공부한 것 정리

## 01. Python
### 01. OS모듈
 - 공식문서 : https://docs.python.org/ko/3/library/os.html?highlight=os#module-os
 - OS모듈은 운영체제의 종속 기능을 사용하기위한 모듈
 - 파일의 입출력은 open() : https://docs.python.org/ko/3/library/functions.html#open
 - 경로 조작과 관련된 것은 os.path() : https://docs.python.org/ko/3/library/os.path.html#module-os.path
 - 환경변수에 관한 내용은 os.environ
  - os.environ은 딕셔너리타입으로 키를 통한 값의 호출이 가능
  - os.environ.get()(os.getenv()) 함수를 사용해 환경변수를 추가하는 것이 가능.  
os.environ.get('key', 'value')같은 방식으로 value의 초기값을 정하는 것이 가능

## 02. Django
### 01. models.django.db의 주요 필드
 ```python
 CharField : 문자열(길이제한 필수)
 IntegerField : wjdtn
 TextField : 문자열(길이제한 필수아님)
 DateField : 날짜
 DateTimeField : 날짜 + 시간
 FileField : 파일
 ImageField : 이미지 파일
 ForeignKey : 외래키(관계)
 OneToOneField : 1대1관계
 MantToManyField : 다대다관계

 # 출처 : 백엔드를 위한 DJANGO REST FRAMEWORK with 파이썬 / 권태형 저 / 영진닷컴
 ```


## 03. DjangoRESTFramework
### 01. DRF의 특징
 - 기존의 PC 웹에 한정된 서비스에서 JSON이나 XML같은 형식의 테이터를 다루는 API서버를 구축하기 위해 생긴 기능
 - Serailizer라는 기능이 특징  
  - DB Data를 JSON Data로 변환(ORM or non-ORM)
  - 다른 네트워크 환경과의 통신에서 직렬화를 담당
  - models에 작성한 폼을 그대로 JSON 형태의 선형정보로 만들어 주는것
   - 참고 : https://velog.io/@ifyouseeksoomi/DRF-Django-REST-Framework-%EA%B0%84%EB%8B%A8%ED%95%9C-%EC%98%88%EC%8A%B5-Serializer


## 04. HTML5