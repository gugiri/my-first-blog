from django.contrib import admin
from .models import Post
# Register your models here.

admin.site.register(Post)   #관리자페이지에서 만든 모델 Post를 볼수 있게 등록
