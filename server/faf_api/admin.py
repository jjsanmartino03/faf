from django.contrib import admin

# Register your models here.

from .models import Categories, Crosses, Matches, Players, Teams, TeamCategories, Users, Validation

admin.site.register(Categories)
admin.site.register(Crosses)
admin.site.register(Matches)
admin.site.register(Players)
admin.site.register(Teams)
admin.site.register(TeamCategories)
admin.site.register(Users)
admin.site.register(Validation)
