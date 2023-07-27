# 일자별 진행 과정
## 23.07.26
 ### AM 09:05 Front와 Back의 구성 기획
 
 ### AM 09:50 Django Model 구성
  #### 01. Django 가상환경구성
   ```shell
   python -m venv venv                                   # python -m venv (가상환경이름) 으로 가상환경 생성
   ./venv/Scripts/Activate.ps1                           # 생성된 가상환경 실행
   (venv) python -m pip install --upgrade pip            # pip 최신버전으로 업그레이드
   (venv) python -m pip install django                   # Django 설치
   (venv) python -m pip install djangorestframework      # DjangoRestFramewokr 설치
   ```
    - 해당 시점의 가상환경의 구성
 
   ```shell
   (venv) python -m pip list                            # pip로 설치한 라이브러리의 목록을 확인
    Package             Version
    ------------------- -------
    asgiref             3.7.2
    Django              4.2.3
    djangorestframework 3.14.0
    pip                 23.2.1
    pytz                2023.3
    setuptools          65.5.0
    sqlparse            0.4.4
    tzdata              2023.3
   ```
 
  #### 02. DjangoApp구성 및 settings.py 기본설정
   ```shell
   (venv) django-admin startproject QnAbot .      # django-admin startproject (프로젝트명) . 을 통해 현재위치에 프로젝트명의 프로젝트 생성 **1 **2
   (venv) django-admin startapp account           # djagno-admin startapp으로 각각의 내부 애플리케이션생성(사용자)
   (venv) djagno-admin startapp GPTQnA            # 해당 프로젝트의 GPT질의를 정리하는 app
   (venv) django-admin startapp post              # GPTQnA를 참조해서 화면으로 출력할 내용을 가공하는 앱
   ```
    - **1 마지막의 . 을 넣지 않을 경우 Projectname/Projectname(생성된프로젝트폴더)의 구조로 생성됨
    - **2 같은 폴더 내에서 프로젝트를 새로 생성할 경우 프로젝트폴더와 manage.py를 같이 삭제하고 첫 줄의 명령어를 다시입력하는 것으로 가능
 
   ```python
   # Application definition
 
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       # django lib
       'rest_framework',
       # django cumtom app
       'account',
       'GPTQnA',
       'post',
   ]
   ```
   - 라이브러리와 생성한 앱을 추가
 
   ```python
   MIDDLEWARE = [
     'django.middleware.security.SecurityMiddleware',
     'django.contrib.sessions.middleware.SessionMiddleware',
     'django.middleware.common.CommonMiddleware',
     'django.middleware.csrf.CsrfViewMiddleware',
     'django.middleware.locale.LocaleMiddleware',
     'django.contrib.auth.middleware.AuthenticationMiddleware',
     'django.contrib.messages.middleware.MessageMiddleware',
     'django.middleware.clickjacking.XFrameOptionsMiddleware',
   ]
   ```
   - 'django.middleware.locale.LocaleMiddleware', 을 통해 번역기능을 준비
 
   ```python
   LANGUAGE_CODE = 'ko-kr'    # django에서 출력할 언어를 한국어로 변경
  
   TIME_ZONE = 'Asia/Seoul'   # djagno에서 사용할 DB의 시간대 설정
  
   USE_I18N = True            # django 번역 시스템 활성화(비활성화는 False)
  
   USE_L10N = True            # django 현지화 데이터 형식 사용(비사용은 False나 없음)
  
   USE_TZ = False              # 시간대 인식 여부 설정(Default는 True)
   ```
   - django의 경우 기본 언어는 'en-us'이고 시간대는 GTP-0를 기준으로 하고 있어 한국에 맞게 변경
   
  - 추후 추가적인 부분들 static, locale, media 등의 필요한 요소는 차후 설정
  - AM 10:20 장고기본설정 완료
  #### AM 10:39 README.md를 좀 더 보기 편하도록 일부 내용을 Wiki로 이동(추후 HTML5를 활용해 정리 할 예정)
  
 ### AM 10:45 migrate 및 runserver로 확인
  ```shell
  python manage.py migrate    # manage.py의 migrate로 db구성
  python manage.py runserver  # manage.py의 runserver로 서버 실행(테스트환경에서만 사용할것을 권장)
  ```

  #### AM 10:50
   - account, GPTQnA, post의 폴더에 forms.py와 urls.py 파일을 생성
   - 각각의 파일은 양식과 url의 목록을 작성

 ### AM 11:00 프로젝트에 필요한 정보 탐색 및 정리
 ### PM 13:34 계획 정리
  #### PM 14:07 MTV를 우선 Django에서 구현한 뒤 Templates를 프론트엔드에서 구현하는 방식으로 진행예정
   - 지난 프로젝트의 실수같이 각 파일들간의 관계 및 모델의 관계에 대한 정리를 더 구체적으로 남겨 추후 생길지 모르는 에러를 예방할 필요가 있음
   - 1차 Django로 대략적인 MTV모델 구성 및 기본 기능 구축
   - 2차 Django에서 DRF로 변환
   - 3차 Templates를 외부 프로젝트로 구축

 ### PM 02:10 1차 Django 시작
  #### PM 14:46 Account, GPTQnA Models.py 기본 형태 구성
  #### PM 14:50 makemigrations 중 account의 모델과 관련된 에러가 발생
   ```shell
    SystemCheckError: System check identified some issues:

    ERRORS:
    account.User.groups: (fields.E304) Reverse accessor 'Group.user_set' for 'account.User.groups' clashes with reverse accessor for 'auth.User.groups'.
        HINT: Add or change a related_name argument to the definition for 'account.User.groups' or 'auth.User.groups'.
    account.User.user_permissions: (fields.E304) Reverse accessor 'Permission.user_set' for 'account.User.user_permissions' clashes with reverse accessor for 'auth.User.user_permissions'.
        HINT: Add or change a related_name argument to the definition for 'account.User.user_permissions' or 'auth.User.user_permissions'.
    auth.User.groups: (fields.E304) Reverse accessor 'Group.user_set' for 'auth.User.groups' clashes with reverse accessor for 'account.User.groups'.
        HINT: Add or change a related_name argument to the definition for 'auth.User.groups' or 'account.User.groups'.
    auth.User.user_permissions: (fields.E304) Reverse accessor 'Permission.user_set' for 'auth.User.user_permissions' clashes with reverse accessor for 'account.User.user_permissions'.
        HINT: Add or change a related_name argument to the definition for 'auth.User.user_permissions' or 'account.User.user_permissions'.
  ```
   - PM 15:04 해결
   ```python
   settings.py
   
   # Auth user
   AUTH_USER_MODEL = 'customUerModel'
   ```
   setttings.py에 해당 코드를 추가하면 해결됨. 유저가 별도로 구현한 User모델을 사용하기 위해서 넣어햐하는데 누락되서 발생함
  #### PM 15:08 manage.py createsuperuser 시 createsuperuser와 account.User사이의 차이로 충돌
   - PM 15:42 account.models의 User클래스에 다음 코드를 추가
   ```python
   models.py
   
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nickname']
   ```
   - PM 15:37 ValueError: localtime() cannot be applied to a naive datetime 발생
   - PM 15:42 UserManager에서 호출한 timezone을 변경
   ```python
   def _create_user(self, **kargs):
        now = timezone.localetime()

   def _create_user(self, **kargs):
        now = timezone.now()
        
   ```

  #### PM 16:43 main, account, post 간의 urls 및 views 기본 양식 구성 후 각각의 이동 확인
  
 ### PM 17:00 DRF로 구성하기전 기본 양식 보완


## 23.07.27
 ### AM 09:05 DRF로 구성하기전 기본 양식 보완 계속
 ### AM 10:00 일부 기능의 기획 변경으로 구조 재정립
  #### PM 13:17 구조를 재정립하는 과정에서 초기화시작
   - 각 기능간의 관계가 기존의 기획에서 다른 방향으로 변경되면서 상대적으로 애플리케이션 간의 관계도가 낮아짐
   - 이미 구현된 모델에서 관계도를 정리하면서 기존의 상태로 돌아올 것을 대비하는 준비
