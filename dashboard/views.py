from django.shortcuts import render
import re

def home(request):

    results = []

    if request.method == 'POST' and request.FILES.get('logfile'):

        logfile = request.FILES['logfile']

        content = logfile.read().decode('utf-8')

        failed_logins = re.findall(
            r'Failed password.*from (\d+\.\d+\.\d+\.\d+)',
            content
        )

        ip_count = {}

        for ip in failed_logins:
            ip_count[ip] = ip_count.get(ip, 0) + 1

        results = ip_count.items()

    return render(request, 'dashboard/home.html', {
        'results': results
    })