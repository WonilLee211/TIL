from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, 
                               on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# 1. db 구성
# 댓글정보를 저장하기 위한 모델 클래스 작성
class Comment(models.Model):
    content = models.CharField(max_length=200)
    # 어떤 게시글에 댓글이 달렸는지 게시글 정보 저장하기 위한 FK
    # FK는 N:1 관계에서 N에 위치
    # 참조할 대상, 대상 삭제시 처리 조건
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, 
                               on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.content