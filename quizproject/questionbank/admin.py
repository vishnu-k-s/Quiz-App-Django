from django.contrib import admin
from .models import *

#registering models
admin.site.register(PythonQBank)
admin.site.register(DjangoQBank)
admin.site.register(QuantitativeQBank)
admin.site.register(JavaQBank)