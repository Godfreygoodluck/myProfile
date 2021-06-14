from django.contrib import admin
from .models import  Message, Contact,Profile, MySkill, What_i_do, Ecommerce, Portfolio, Blog

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >=1:
            return False
        else:
            return True

class ContactAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >=1:
            return False
        else:
            return True

class What_i_doAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >=3:
            return False
        else:
            return True

class EcommerceAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >=3:
            return False
        else:
            return True

class PortfolioAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >=3:
            return False
        else:
            return True

class BlogAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >=3:
            return False
        else:
            return True


admin.site.register(Ecommerce, EcommerceAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Message)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(MySkill)
admin.site.register(What_i_do, What_i_doAdmin)