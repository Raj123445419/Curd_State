from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect
from .models import Country, State, City, userSelation



from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect
from .models import Country, State, City

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_per_page = 30
    
    def get_urls(self):
        urls = super().get_urls()
        # Custom URL for Colon Parser
        custom_urls = [
            path('import-data/', self.admin_site.admin_view(self.import_states_cities), name='import_states_cities'),
        ]
        return custom_urls + urls

    def import_states_cities(self, request):
        if request.method == 'POST':
            country_id = request.POST.get('country')
            raw_text = request.POST.get('raw_text')
            if country_id and raw_text:
                country = Country.objects.get(id=country_id)
                for line in raw_text.strip().split('\n'):
                    if ':' in line:
                        parts = line.split(':', 1)
                        state_obj, _ = State.objects.get_or_create(name=parts[0].strip(), country=country)
                        city_names = [c.strip() for c in parts[1].replace(',', '\n').split('\n') if c.strip()]
                        for c_name in city_names:
                            City.objects.get_or_create(name=c_name, state=state_obj)
                self.message_user(request, "Data successfully imported!")
                return redirect('..')
        return render(request, 'admin/import_data.html', {'countries': Country.objects.all(), 'opts': self.model._meta})


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']
    search_fields = ['name', 'country__name']
    list_per_page = 30
    
    def get_urls(self):
        urls = super().get_urls()
        # URL changed to bulk-add
        custom_urls = [
            path('bulk-add/', self.admin_site.admin_view(self.bulk_add_states), name='bulk_add_states'),
        ]
        return custom_urls + urls

    def bulk_add_states(self, request):
        if request.method == 'POST':
            country = Country.objects.get(id=request.POST.get('country'))
            for name in [s.strip() for s in request.POST.get('states_text').replace(',', '\n').split('\n') if s.strip()]:
                State.objects.get_or_create(name=name, country=country)
            self.message_user(request, "States added successfully!")
            return redirect('..')
        return render(request, 'admin/bulk_add_states.html', {'countries': Country.objects.all(), 'opts': self.model._meta})


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'state']
    search_fields = ['name', 'state__name']
    list_per_page = 30
    
    def get_urls(self):
        urls = super().get_urls()
        # URL changed to bulk-add
        custom_urls = [
            path('bulk-add/', self.admin_site.admin_view(self.bulk_add_cities), name='bulk_add_cities'),
        ]
        return custom_urls + urls

    def bulk_add_cities(self, request):
        if request.method == 'POST':
            state = State.objects.get(id=request.POST.get('state'))
            for name in [c.strip() for c in request.POST.get('cities_text').replace(',', '\n').split('\n') if c.strip()]:
                City.objects.get_or_create(name=name, state=state)
            self.message_user(request, "Cities added successfully!")
            return redirect('..')
        return render(request, 'admin/bulk_add_cities.html', {'states': State.objects.all(), 'opts': self.model._meta})









admin.site.register(userSelation)