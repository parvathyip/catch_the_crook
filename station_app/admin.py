from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Login_Table)
admin.site.register(Register_station)
admin.site.register(Register_dgp)
admin.site.register(Register_wanted)
admin.site.register(Register_public)
admin.site.register(Add_complaint)