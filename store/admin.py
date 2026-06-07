from django.contrib import admin
from .models import Product, Cart, CartItem, Feedback, Order, OrderItem

# Product ke liye custom admin view
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category'] 
    search_fields = ['name'] 
    list_filter = ['category'] # Isse category ke hisaab se filter karne ka option aayega

# Cart ke liye custom admin view
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user'] 

# CartItem ke liye custom admin view
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'product', 'quantity']

# Feedback Admin 
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    search_fields = ['name', 'email'] 

# NAYA: Order Admin (Jisse dashboard mein orders achhe se dikhein)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'full_name', 'city', 'total_amount', 'created_at']
    search_fields = ['full_name', 'phone', 'city'] # Naam ya phone number se order search kar payenge
    list_filter = ['created_at', 'city'] # Date ya city ke hisaab se orders filter kar payenge

# NAYA: Order Item Admin (Ek order ke andar kya-kya products hain)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price']

# Models ko unke custom admin classes ke sath register karna
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Order, OrderAdmin)        # Order model register ho gaya
admin.site.register(OrderItem, OrderItemAdmin) # OrderItem model register ho gaya