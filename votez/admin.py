from django.contrib import admin

# Register your models here.


from .models import Vote,LevelOfAppreciation

admin.site.register(Vote)

admin.site.register(LevelOfAppreciation)