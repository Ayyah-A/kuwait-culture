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
    counselor_emp = Employee.objects.filter(publish=True, department='Cultural Counselor’s Office').exclude(job_title='Cultural Counselor/Director').order_by('first_name')
    attaches = Employee.objects.filter(publish=True, department='Cultural Attache’s Office', job_title='Cultural Attache').order_by('first_name')
    attache_emp = Employee.objects.filter(publish=True, department='Cultural Attache’s Office').exclude(job_title='Cultural Attache').order_by('first_name')
    acct_emp = Employee.objects.filter(publish=True, department='Accounting').exclude(job_title='Director').order_by('first_name')
    acct_dir = Employee.objects.filter(publish=True, department='Accounting',job_title='Director').order_by('first_name')
    admi_dir = Employee.objects.filter(publish=True, department='Administration', job_title='Director').order_by('first_name')
    admi_emp = Employee.objects.filter(publish=True, department='Administration').exclude(job_title='Director').order_by('first_name')
    auth_dir = Employee.objects.filter(publish=True, department='Authentication', job_title='Director').order_by('first_name')
    auth_emp = Employee.objects.filter(publish=True, department='Authentication').exclude(job_title='Director').order_by('first_name')
    grad_dir = Employee.objects.filter(publish=True, department='Graduate', job_title='Director').order_by('first_name')
    grad_emp = Employee.objects.filter(publish=True, department='Graduate').exclude(job_title='Director').order_by('first_name')
    undergrad_dir = Employee.objects.filter(publish=True, department='Undergraduate', job_title='Director').order_by('first_name')
    undergrad_emp = Employee.objects.filter(publish=True, department='Undergraduate').exclude(job_title='Director').order_by('first_name')
    tran_dir = Employee.objects.filter(publish=True, department='Translation', job_title='Director').order_by('first_name')
    tran_emp = Employee.objects.filter(publish=True, department='Translation').exclude(job_title='Director').order_by('first_name')
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
        'counselor_emp': counselor_emp,
        'attaches': attaches,
        'attache_emp': attache_emp,
        'acct_emp': acct_emp,
        'acct_dir': acct_dir,
        'admi_dir': admi_dir,
        'admi_emp': admi_emp,
        'auth_dir': auth_dir,
        'auth_emp': auth_emp,
        'grad_dir': grad_dir,
        'grad_emp': grad_emp,
        'undergrad_dir': undergrad_dir,
        'undergrad_emp': undergrad_emp,
        'tran_dir': tran_dir,
        'tran_emp': tran_emp,
        'it_emp': it_emp,
        'it_dir': it_dir,
    }
    return render(request, 'pages/contacts.html', my_employee)


def test(request):
    # Page from the theme
    return render(request, 'pages/test.html')