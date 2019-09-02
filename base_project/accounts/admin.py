from django.contrib import admin
from .models import Profile


class AccountAdmin(admin.ModelAdmin):
    ordering = ('-paid',)
    list_display = ('__str__', 'course', 'register', 'subscription_cost', 'paid')
    list_filter = ('course', 'lectures',)
    search_fields = ('owner__first_name', 'owner__last_name')

    def subscription_cost(self, obj):
        return obj.calc_sub_cost()


admin.site.register(Profile)
# Register your models here.
