from django.http import HttpResponse


def home_page_view(request):
    print('testing')
    return HttpResponse('Hello, Worldd')
