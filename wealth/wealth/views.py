from django.shortcuts import render


def deshboard(request):
    return render(request, "pages/dashboard.html")