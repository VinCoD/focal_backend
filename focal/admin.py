from django.contrib import admin
from .models import Vision, Mission, CustomerSatisfaction


# Register your models here.

admin.site.register(Vision)
admin.site.register(Mission)
admin.site.register(CustomerSatisfaction)