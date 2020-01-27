from django.contrib import admin
from .models import *

class SliderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Slider._meta.fields]

    class Meta:
        model = Slider

admin.site.register(Slider, SliderAdmin)

class ResultBeyoundAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ResultBeyond._meta.fields]

    class Meta:
        model = ResultBeyond

admin.site.register(ResultBeyond, ResultBeyoundAdmin)

class LogoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in LogoSlider._meta.fields]

    class Meta:
        model = LogoSlider

admin.site.register(LogoSlider, LogoAdmin)

class About_Us_Admin(admin.ModelAdmin):
    list_display = [field.name for field in About_Us._meta.fields]

    class Meta:
        model = About_Us

admin.site.register(About_Us, About_Us_Admin)