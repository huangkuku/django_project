from django.contrib import admin
from .models import Member

# Set list_display Create a MemberAdmin() class and specify the list_display tuple
class MemberAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'join_date')
    prepopulated_fields = {'slug':('firstname', 'lastname')}

admin.site.register(Member, MemberAdmin)