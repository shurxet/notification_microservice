from django.http import JsonResponse


def root_domain(request):
    return JsonResponse({'STATUS': 'OK'})
