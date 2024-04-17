from django.contrib import admin
from .models import Document


# Register your models here.
@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('doc_name', 'published', 'important_doc')
