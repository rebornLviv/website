from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField

class Slider(models.Model):
    title = models.CharField(default=None, max_length=64)
    description = HTMLField(default=None)
    image = models.ImageField(upload_to='images/')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Slide'
        verbose_name_plural = 'Slides'

class LogoSlider(models.Model):
    image = models.ImageField(upload_to='images/')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Logo Slider'
        verbose_name_plural = 'Logo Slider'

class About_Us(models.Model):
    description = HTMLField(default=None)

    class Meta:
        verbose_name = 'About us'
        verbose_name_plural = 'About us'

class ResultBeyond(models.Model):
    image = models.ImageField(upload_to='images/')
    description = HTMLField(default=None)
    url = models.URLField(default=None)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Result Beyond'
        verbose_name_plural = 'Results Beyond'

class InnovationBeyond(models.Model):

    description = HTMLField(default=None)
    url = models.URLField(default=None)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Result Beyond'
        verbose_name_plural = 'Results Beyond'

class Order(models.Model):
    name = models.CharField(help_text='Your Name', max_length=128)
    email = models.EmailField(help_text='Your Email')
    phone = models.CharField(help_text='Your Phone', max_length=128, default=None, null=True)
    message = models.CharField(help_text='Your Message', max_length=528)

    def __str__(self):
        return "Order %s %s" % (self.name, self.email)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'