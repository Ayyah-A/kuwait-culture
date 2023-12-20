from django.shortcuts import render
from django.http import HttpResponse
from employees.models import Employee
from cards.models import Card

# Create your views here.

def index(request):
    # Page from the theme
    return render(request, 'pages/index.html')
def mohe(request):
    mohe_cards = Card.objects.filter(card_visible=True,sponsor='mohe')

    cards = {
        'mohe_cards': mohe_cards,
    }
    # Page from the theme
    return render(request, 'pages/mohe.html', cards)

def kuwait_university(request):
    ku_cards = Card.objects.filter(card_visible=True, sponsor='kuwait university')

    cards = {
        'ku_cards': ku_cards,
    }
    # Page from the theme
    return render(request, 'pages/kuwait_university.html', cards)

def contacts(request):
    obj = Employee.objects.get(id=1)
    counselor_dir = Employee.objects.filter(publish=True, department='cultural counselor’s office', job_title='Cultural Counselor/Director').order_by('first_name')
    counselor_emp = Employee.objects.filter(publish=True, department='cultural counselor’s office').exclude(job_title='Cultural Counselor/Director').order_by('first_name')
    attaches = Employee.objects.filter(publish=True, department='cultural attache’s office', job_title='Cultural Attache').order_by('first_name')
    attache_emp = Employee.objects.filter(publish=True, department='cultural attache’s office').exclude(job_title='Cultural Attache').order_by('first_name')
    acct_emp = Employee.objects.filter(publish=True, department='accounting').exclude(job_title='Director').order_by('first_name')
    acct_dir = Employee.objects.filter(publish=True, department='accounting',job_title='Director').order_by('first_name')
    admi_dir = Employee.objects.filter(publish=True, department='administration', job_title='Director').order_by('first_name')
    admi_emp = Employee.objects.filter(publish=True, department='administration').exclude(job_title='Director').order_by('first_name')
    auth_dir = Employee.objects.filter(publish=True, department='authentication', job_title='Director').order_by('first_name')
    auth_emp = Employee.objects.filter(publish=True, department='authentication').exclude(job_title='Director').order_by('first_name')
    grad_dir = Employee.objects.filter(publish=True, department='graduate', job_title='Director').order_by('first_name')
    grad_emp = Employee.objects.filter(publish=True, department='graduate').exclude(job_title='Director').order_by('first_name')
    undergrad_dir = Employee.objects.filter(publish=True, department='undergraduate', job_title='Director').order_by('first_name')
    undergrad_emp = Employee.objects.filter(publish=True, department='undergraduate').exclude(job_title='Director').order_by('first_name')
    tran_dir = Employee.objects.filter(publish=True, department='translation', job_title='Director').order_by('first_name')
    tran_emp = Employee.objects.filter(publish=True, department='translation').exclude(job_title='Director').order_by('first_name')
    it_emp = Employee.objects.filter(publish=True, department='information technology').exclude(job_title='Director').order_by('first_name')
    it_dir = Employee.objects.filter(publish=True, department='information technology', job_title='Director').order_by('first_name')

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
