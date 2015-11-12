from django.contrib import admin
from .models import Participant, Week


# Register your models here.

class WeeksInline(admin.StackedInline):
    model = Week
    extra = 6


class ParticipantAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Participant Name", {'fields': ['part_name']}),
    ]
    inlines = [WeeksInline]


admin.site.register(Participant, ParticipantAdmin)
