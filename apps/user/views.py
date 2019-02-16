from django.shortcuts import HttpResponse


# Create your views here.
def user_center(requset):
    return HttpResponse("user_center")


def edit_user(request):
    return HttpResponse("edit_user")
