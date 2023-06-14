from django.db import models


class Customer(models.Model):
    customer_name = models.CharField(max_length=50)
    customer_email = models.EmailField(max_length=254)
    customer_address = models.TextField()

class Game(models.Model):
    game_name = models.CharField(max_length=50)
    game_price = models.IntegerField()
    game_desc = models.TextField()
    game_platforms = models.TextField()
    game_company = models.CharField(max_length=50)
    game_image = models.ImageField()

class Order(models.Model):
    order_date = models.DateTimeField()

class News(models.Model):
    news_title = models.TextField()
    news_content = models.TextField()
    news_link = models.TextField()
