from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from core import settings
from django.http import HttpResponse
from employees.models import Employee
from cards.models import Card
from announce.models import Announcement
from .models import Document

from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView, PasswordResetConfirmView
from core.forms import RegistrationForm, UserLoginForm, UserPasswordResetForm, UserSetPasswordForm, UserPasswordChangeForm
from django.contrib.auth import logout

# Create your views here.
def index(request):
    headline = Announcement.objects.filter(homepage_headline=True)
    important_announce = Announcement.objects.filter(publish=True, important=True).order_by('-post_date')[:5]
    sponsor_cards = Card.objects.filter(card_visible=True, sponsor='all', page='homepage')

    homepage = {
        'headline': headline,
        'important_announce': important_announce,
        'sponsor_cards': sponsor_cards,
    }

    # Page from the theme
    return render(request, 'pages/index.html', homepage)

def students(request):
    resource_cards = Card.objects.filter(card_visible=True, sponsor='all', page='students')

    student_cards = {
        'resource_cards': resource_cards,
    }
    # Page from the theme
    return render(request, 'pages/students.html', student_cards)


def documents(request):
    documents = Document.objects.filter(published=True).order_by('doc_name')
    important_documents = Document.objects.filter(published=True, important_doc=True).order_by('doc_name')[:5]
    page = request.GET.get('page',1)

    paginator = Paginator(documents, 10)
    try:
        docs = paginator.page(page)
    except PageNotAnInteger:
        docs = paginator.page(1)
    except EmptyPage:
        docs = paginator.page(paginator.num_pages)


    student_documents = {
        'documents': documents,
        'important_documents': important_documents,
        'docs': docs,
    }
    # Page from the theme
    return render(request, 'pages/documents.html', student_documents)

def announcements(request):
    announcement_rec = Announcement.objects.filter(publish=True).order_by('-post_date')
    important_announce = Announcement.objects.filter(publish=True, important=True).order_by('-post_date')[:4]
    page = request.GET.get('page', 1)

    paginator = Paginator(announcement_rec, 6)
    try:
        announces = paginator.page(page)
    except PageNotAnInteger:
        announces = paginator.page(1)
    except EmptyPage:
        announces = paginator.page(paginator.num_pages)

    active_announcement = {
        'announcement_rec': announcement_rec,
        'important_announce': important_announce,
        'announces': announces,
    }
    # Page from the theme
    return render(request, 'pages/announcements.html', active_announcement)

def contacts(request):
    obj = Employee.objects.get(id=1)
    counselor_dir = Employee.objects.filter(publish=True, department='cultural_counselor_office', job_title='Cultural Counselor/Director').order_by('first_name')
    counselor_emp = Employee.objects.filter(publish=True, department='cultural_counselor_office').exclude(job_title='Cultural Counselor/Director').order_by('first_name')
    attaches = Employee.objects.filter(publish=True, department='cultural_attache_office', job_title='Cultural Attache').order_by('first_name')
    attache_emp = Employee.objects.filter(publish=True, department='cultural_attache_office').exclude(job_title='Cultural Attache').order_by('first_name')
    acct_emp = Employee.objects.filter(publish=True, department='accounting').exclude(job_title='Director').order_by('first_name')
    acct_dir = Employee.objects.filter(publish=True, department='accounting',job_title='Director').order_by('first_name')
    admi_dir = Employee.objects.filter(publish=True, department='administration', job_title='Director').order_by('first_name')
    admi_emp = Employee.objects.filter(publish=True, department='administration').exclude(job_title='Director').order_by('first_name')
    auth_dir = Employee.objects.filter(publish=True, department='placement', job_title='Director').order_by('first_name')
    auth_emp = Employee.objects.filter(publish=True, department='placement').exclude(job_title='Director').order_by('first_name')
    prog_dir = Employee.objects.filter(publish=True, department='program_eval', job_title='Director').order_by('first_name')
    prog_emp = Employee.objects.filter(publish=True, department='program_eval').exclude(job_title='Director').order_by('first_name')
    grad_dir = Employee.objects.filter(publish=True, department='graduate', job_title='Director').order_by('first_name')
    grad_emp = Employee.objects.filter(publish=True, department='graduate').exclude(job_title='Director').order_by('first_name')
    undergrad_dir = Employee.objects.filter(publish=True, department='undergraduate', job_title='Director').order_by('first_name')
    undergrad_emp = Employee.objects.filter(publish=True, department='undergraduate').exclude(job_title='Director').order_by('first_name')
    tran_dir = Employee.objects.filter(publish=True, department='translation', job_title='Director').order_by('first_name')
    tran_emp = Employee.objects.filter(publish=True, department='translation').exclude(job_title='Director').order_by('first_name')
    it_emp = Employee.objects.filter(publish=True, department='information_technology').exclude(job_title='Director').order_by('first_name')
    it_dir = Employee.objects.filter(publish=True, department='information_technology', job_title='Director').order_by('first_name')

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
        'prog_dir': prog_dir,
        'prog_emp': prog_emp,
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

def civil_service(request):
    cs_cards = Card.objects.filter(card_visible=True, sponsor='civil service')

    cards = {
        'cs_cards': cs_cards,
    }
    # Page from the theme
    return render(request, 'pages/civil_service.html', cards)

def paaet(request):
    paaet_cards = Card.objects.filter(card_visible=True, sponsor='paaet')

    cards = {
        'paaet_cards': paaet_cards,
    }
    # Page from the theme
    return render(request, 'pages/paaet.html', cards)

def kuwait_authority(request):
    kia_cards = Card.objects.filter(card_visible=True, sponsor='kuwait investment authority')

    cards = {
        'kia_cards': kia_cards,
    }
    # Page from the theme
    return render(request, 'pages/kuwait_authority.html', cards)


def positions(request):
    documents = Document.objects.filter(published=True).order_by('doc_name')
    important_documents = Document.objects.filter(published=True, important_doc=True).order_by('doc_name')[:5]
    page = request.GET.get('page', 1)

    paginator = Paginator(documents, 10)
    try:
        docs = paginator.page(page)
    except PageNotAnInteger:
        docs = paginator.page(1)
    except EmptyPage:
        docs = paginator.page(paginator.num_pages)

    student_documents = {
        'documents': documents,
        'important_documents': important_documents,
        'docs': docs,
    }
    return render(request, 'pages/positions.html', student_documents)



# Authentication

def register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      print("Account created successfully!")
      return redirect('/accounts/login')
    else:
      print("Registration failed!")
  else:
    form = RegistrationForm()

  context = { 'form': form }
  return render(request, 'accounts/sign-up.html', context)


class UserLoginView(LoginView):
  template_name = 'account/sign-in.html'
  form_class = UserLoginForm

def logout_view(request):
  logout(request)
  return redirect('/accounts/login')

class UserPasswordResetView(PasswordResetView):
  template_name = 'accounts/password_reset.html'
  form_class = UserPasswordResetForm

class UserPasswordResetConfirmView(PasswordResetConfirmView):
  template_name = 'accounts/password_reset_confirm.html'
  form_class = UserSetPasswordForm

class UserPasswordChangeView(PasswordChangeView):
  template_name = 'accounts/password_change.html'
  form_class = UserPasswordChangeForm

