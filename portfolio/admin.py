from django.contrib import admin
from .models import Project,Company
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('title','description','user','created','project_companies')
    ordering = ('user','created',)
    search_fields = ('title','description','user__username','companies__name')
    date_hierarchy = 'created'
    list_filter = ('user__username','companies__name') #filtrado por relaciones por ejemplo user u otro catalogo

    def project_companies(self,obj):
        return ",".join([c.name for c in obj.companies.all().order_by('name')])

    project_companies.short_description = "Empresas"

class CompanyAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Project,ProjectAdmin)
admin.site.register(Company,CompanyAdmin)
