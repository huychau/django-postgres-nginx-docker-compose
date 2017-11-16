from django.contrib import admin

from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    """Employee admin"""

    list_display = ('first_name', 'last_name', 'birthday', 'gender', 'email', 'status')
    search_fields = ('first_name', 'last_name', 'email')
    
admin.site.register(Employee, EmployeeAdmin)
