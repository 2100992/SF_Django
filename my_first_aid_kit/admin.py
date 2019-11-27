from django.contrib import admin

from codecs import register

from my_first_aid_kit.models import *

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Drugmaker)
class DrugmakerAdmin(admin.ModelAdmin):
    pass

@admin.register(Medicament)
class MedicamentAdmin(admin.ModelAdmin):
    pass

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass

@admin.register(ActiveSubstance)
class ActiveSubstancedmin(admin.ModelAdmin):
    pass

@admin.register(PharmaGroup)
class PharmaGroupAdmin(admin.ModelAdmin):
    pass