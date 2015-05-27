from django.contrib import admin

# Register your models here.


from .models import Team







class TeamAdmin(admin.ModelAdmin):
    list_display = ('name','teamMatez')

    def teamMatez(self, obj):
        return ",".join([k.user.username for k in obj.teammate_set.all()])

admin.site.register(Team,TeamAdmin)