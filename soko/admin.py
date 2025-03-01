from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Comment,Customer,Product,Location,Order,Reply

admin.site.site_header = "Soko Admin Panel"
admin.site.site_title = "Soko Admin"
admin.site.index_title = "Welcome to the Soko Admin Dashboard"


#add class Model to Admin Dashboard
admin.site.register(Customer,UserAdmin)
admin.site.register(Comment)
admin.site.register(Product)
admin.site.register(Location)
admin.site.register(Order)
admin.site.register(Reply)
