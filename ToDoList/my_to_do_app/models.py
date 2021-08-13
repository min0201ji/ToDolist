from django.db import models

# Create your models here.
class Todo(models.Model): # models.Model 을 상속받아 Django 모델 class 생성
    # 컬럼 지정
    content = models.CharField(max_length=255) # 교재 175쪽

# 모델 수정시 아래 두 명령어를 반드시 진행하고 다음 코딩으로 넘어가야 함
    # 나) 모델의
    # 변경사항
    # 추출
    # python manage.py makemigrations

    # 다) 변경된
    # 모델
    # 사항
    # DB에
    # 반영
    # python manage.py migrate