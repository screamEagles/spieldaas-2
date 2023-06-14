from django.contrib import admin
from spieldaas.models import Customer, Game, News

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=('customer_name', 'customer_email', 'customer_address')

class Games(admin.ModelAdmin):
    list_display=('game_name', 'game_price', 'game_desc', 'game_platforms', 'game_company', 'game_image')

class NewsSection(admin.ModelAdmin):
    list_display=('news_title', 'news_content', 'news_link')


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Game, Games)
admin.site.register(News, NewsSection)
