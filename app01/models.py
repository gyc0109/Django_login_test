from django.db import models

# Create your models here.
class User(models.Model):
    """ 用户登录表 """

    # unique 唯一, 不允许重复
    username = models.CharField(verbose_name="用户名", max_length=32, unique=True)
    password = models.CharField(verbose_name="密码", max_length=64)
