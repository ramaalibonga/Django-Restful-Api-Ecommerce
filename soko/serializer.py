from rest_framework import  serializers
from .models import Customer,Comment,Product,Order,Location,Reply


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    location_order  =  LocationSerializer(many=True,read_only=True)
    class Meta:
        model = Order
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    order_product  = OrderSerializer(many=True,read_only=True)
   
    class Meta:
        model = Product
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    product_customer  = ProductSerializer(many=True)
    comment_customer  = CommentSerializer(many=True)
    class Meta:
        model = Customer
        fields = ["username", "email","phone","product_customer","comment_customer"]

    def create(self, validated_data):
        product_customers_data = validated_data.pop('product_customer')
        customer = Customer.objects.create(**validated_data)
        for product_customer_data in product_customers_data:
            Product.objects.create(customer=customer, **track_data)
        return customer



class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'