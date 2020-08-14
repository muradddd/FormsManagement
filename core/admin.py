from django.contrib import admin
from core.models import *




class OptionInline(admin.StackedInline):
    model = Option


class FieldInline(admin.StackedInline):
    model = Field


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    fieds = ('__all__')


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    fieds = ('__all__')

class ResponsenInline(admin.TabularInline):
    model = ResponseQA

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    fieds = ('__all__')
    inlines = [ResponsenInline,]


@admin.register(Forms)
class FormAdmin(admin.ModelAdmin):
    inlines = [FieldInline,]