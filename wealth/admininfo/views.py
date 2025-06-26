from django.shortcuts import render

# Create your views here.
def adminpanel(request):
    return render(request, "admin-panel.html")

def adminchat(request):
    return render(request,"chat-admin.html")
