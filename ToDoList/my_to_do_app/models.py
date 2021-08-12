from django.db import models

# Create your models here.
class Todo(models.Model): # models.Model 을 상속받아 Django 모델 class 생성
    # 컬럼 지정
    content = models.CharField(max_length=255) # 교재 175쪽