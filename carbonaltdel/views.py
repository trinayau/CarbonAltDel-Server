from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello! You're at the wwww.carbonaltdel.com Django REST API. In the future, you will not be able to access this page. Please use the API endpoints instead.")
