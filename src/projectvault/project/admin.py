from django.contrib import admin
from models import *


class RepresentationalImageAdmin(admin.StackedInline):
    model = RepresentationalImage
    prepopulated_fields = {"slug": ("text",)}


class FeatureAdmin(admin.StackedInline):
    model = Feature
    prepopulated_fields = {"slug": ("text",)}


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = None

    inlines = [
                RepresentationalImageAdmin,
                FeatureAdmin
            ]
admin.site.register(Project, ProjectAdmin)
