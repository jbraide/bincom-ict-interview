from django.contrib import admin
from .models import *

@admin.register(AgentName)
class AgentNameAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname']

@admin.register(AnnouncedLgaResult)
class AnnouncedLgaResultAdmin(admin.ModelAdmin):
    list_display = ['lga_name', 'party_abbreviation']

@admin.register(AnnouncedPuResult)
class AnnouncedPuResultAdmin(admin.ModelAdmin):
    list_display = ['result_id', 'polling_unit_uniqueid']

@admin.register(AnnouncedStateResult)
class AnnouncedStateResultAdmin(admin.ModelAdmin):
    list_display = ['result_id']

@admin.register(AnnouncedWardResult)
class AnnouncedWardResultAdmin(admin.ModelAdmin):
    list_display = ['result_id']

@admin.register(Lga)
class LgaAdmin(admin.ModelAdmin):
    list_display = ['uniqueid', 'lga_id', 'lga_name']

@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(PollingUnit)
class PollingUnitAdmin(admin.ModelAdmin):
    list_display = ['uniqueid', 'lga_id', 'polling_unit_id', 'polling_unit_number']

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['state_id']

@admin.register(Ward)
class WardAdmin(admin.ModelAdmin):
    list_display = ['uniqueid']
