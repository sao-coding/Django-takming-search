from django.shortcuts import render
from api import models
from django.contrib import auth
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes

# Create your views here.

@api_view(["GET"])
def api(request):
    return Response({"message": "Hello, World!"})

@api_view(["POST"])
@permission_classes([AllowAny])
@authentication_classes([])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = auth.authenticate(username=username, password=password)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"status": "success", "token": token.key}, status=200)
    else:
        return Response({"status": "fail"}, status=401)

@api_view(["POST"])
def logout(request):
    request.user.auth_token.delete()
    return Response(status=204)

@api_view(["POST"])
@permission_classes([AllowAny])
@authentication_classes([])
def authtoken(request):
    token = request.headers.get("Authorization")
    try:
        token = Token.objects.get(key=token)
        return Response({"status": "success"}, status=200)
    except:
        return Response({"status": "fail"}, status=401)

@api_view(["POST"])
@permission_classes([AllowAny])
# @authentication_classes([])
def bed_search(request):
    token = request.data.get("token")
    bed = request.data.get("bed")
    # member_info = models.Member_info.objects.filter(bed__contains=bed).values()
    # print(member_info[0]["student_ID"])
    try:
        token = Token.objects.get(key=token)
        member_info = models.Member_info.objects.filter(bed__contains=bed).values()
        img = "https://tipfile.takming.edu.tw/stuphoto/"
        # info = []
        # for i in range(len(member_info)):
        #     info.append(
        #         {
        #             "id": member_info[i]['id'],
        #             "照片": img + member_info[i]['student_ID'] + ".jpg",
        #             "國家": member_info[i]['country'],
        #             "房間": member_info[i]['room'],
        #             "床號": member_info[i]['bed'],
        #             "班級": member_info[i]['member_class'],
        #             "學號": member_info[i]['student_ID'],
        #             "姓名": member_info[i]['name'],
        #             "身分證號碼": member_info[i]['ID_number'],
        #             "生日": member_info[i]['birthday'],
        #             "電話": member_info[i]['phone'],
        #             "家電": member_info[i]['home_phone'],
        #             "戶籍地址": member_info[i]['address'],
        #             "緊急聯絡人": member_info[i]['emergency_contact'],
        #             "緊急聯絡人電話": member_info[i]['emergency_contact_phone'],
        #         }
        #     )
        for i in range(len(member_info)):
            member_info[i]["photo"] = img + member_info[i]['student_ID'] + ".jpg"
        print(member_info)
        
        return Response({"status": "success", "info": member_info}, status=200)
    except:
        return Response({"status": "fail"}, status=401)


# {
# "token":"fb679e648230d18367a3f86cbea60f7eba9a62cb",
# "bed":"107"
# }