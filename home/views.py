from django.shortcuts import render
from django.http import HttpResponse
from employees.models import Employee

# Create your views here.

def index(request):
    # Page from the theme
    return render(request, 'pages/index.html')

def contacts(request):
    obj = Employee.objects.get(id=1)
    counselor_dir = Employee.objects.filter(publish=True, department='Cultural Counselor’s Office', job_title='Cultural Counselor/Director').order_by('first_name')
    attaches = Employee.objects.filter(publish=True, department='Cultural Attache’s Office', job_title='Cultural Attache').order_by('first_name')
    acct_emp = Employee.objects.filter(publish=True, department='Accounting').exclude(job_title='Director').order_by('first_name')
    acct_dir = Employee.objects.filter(publish=True, department='Accounting',job_title='Director').order_by('first_name')
    it_emp = Employee.objects.filter(publish=True, department='Information Technology').exclude(job_title='Director').order_by('first_name')
    it_dir = Employee.objects.filter(publish=True, department='Information Technology', job_title='Director').order_by('first_name')

    # my_employee = {
    #     "full_name": employee.first_name + " " + employee.last_name,
    #     "job_title": "JOB",
    #     "email": "test@email.com"
    # }

    my_employee = {
        'employee': obj,
        'counselor_dir': counselor_dir,
        'attaches': attaches,
        'acct_emp': acct_emp,
        'acct_dir': acct_dir,
        'it_emp': it_emp,
        'it_dir': it_dir,
    }
    return render(request, 'pages/contacts.html', my_employee)


def test(request):
    # Page from the theme
    return render(request, 'pages/test.html')