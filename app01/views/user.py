from app01 import models
from django import forms
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from app01.utils.bootstrap import BootStrapModelForm
from app01.utils.pagination import Pagination


class UserModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(label="确认密码", widget=forms.PasswordInput)

    class Meta:
        model = models.User
        fields = ["username", "password", "confirm_password"]
        widgets = {
            "password": forms.PasswordInput,
        }


def user_manage(request):
    """ 用户管理列表 """
    queryset = models.User.objects.all()
    page_object = Pagination(request, queryset)
    form = UserModelForm()
    context = {
        "form": form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }

    return render(request, "user_manage.html", context)


@csrf_exempt
def user_add(request):
    """ 添加用户 """
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        # 保存到数据库
        print(form.cleaned_data)
        form.save()
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, "error": form.errors})

def user_delete(request):
    """ 删除用户 """
    uid = request.GET.get("uid")
    print(uid)
    # 判断是否存在
    exists = models.User.objects.filter(id=uid).exists()
    if not exists:
        return JsonResponse({"status": False, "error": "用户不存在"})

    models.User.objects.filter(id=uid).delete()
    return JsonResponse({"status": True})

def login(request):
    return render(request, "login.html")

