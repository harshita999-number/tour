from django.contrib import admin
from myapp.models import Booknow, Contact, roomBook


# Register your models here.
admin.site.register(Contact)

class BooknowAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    
admin.site.register(Booknow, BooknowAdmin)

class roomBookAdmin(admin.ModelAdmin):
        readonly_fields = ('created_at',)

admin.site.register(roomBook, roomBookAdmin)


