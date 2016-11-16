from django.contrib import admin

from moments.models import Moment, MomentsCollection


# Register your models here.
admin.site.register(Moment)
admin.site.register(MomentsCollection)
