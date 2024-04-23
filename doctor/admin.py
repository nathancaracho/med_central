from django.contrib import admin

from doctor.models import Doctor, Crm, PhoneNumber, OfficeAddress

admin.site.register(Doctor)
admin.site.register(Crm)
admin.site.register(PhoneNumber)
admin.site.register(OfficeAddress)
