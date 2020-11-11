from django.contrib import admin
from testApp.models import hydjobs,ban,chennai,delhi

# Register your models here.
class hydAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phoneNumber']

class banAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phoneNumber']

class chennaiAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phoneNumber']

class delhiAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phoneNumber']

admin.site.register(hydjobs,hydAdmin)
admin.site.register(ban,banAdmin)
admin.site.register(chennai,chennaiAdmin)
admin.site.register(delhi,delhiAdmin)