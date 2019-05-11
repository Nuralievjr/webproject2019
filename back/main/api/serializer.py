from rest_framework import serializers
from api.models import Category,ContactModel,Product
from django.contrib.auth.models import User


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    def create(self, validated_data):
        # {'name': 'new category 3'}
        # name='new category 3'
        category = Category(**validated_data)
        category.save()
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class CategorySerializerModel(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    class Meta:
        model = Category
        fields = ('id', 'name')
        # fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'count', 'image', 'category', 'visit', 'description')



class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactModel
        fields = ('name', 'email', 'phone', 'message')
        # fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email',)