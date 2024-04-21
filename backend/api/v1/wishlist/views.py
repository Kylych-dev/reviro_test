from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.wishlist.models import WishlistItem
from .serializers import WishlistItemSerializer

from apps.product.models import Product



class WishlistModelViewSet(viewsets.ModelViewSet):
	queryset = WishlistItem.objects.all()
	serializer_class = WishlistItemSerializer
	permission_classes = [IsAuthenticated,]
	# permission_classes = [AllowAny,]

	@action(detail=False, methods=["post"])
	def add_wishlist(self, request, *args, **kwargs):
		pid = request.data.get('product')
		product = get_object_or_404(Product, pk=pid)
		if WishlistItem.objects.filter(product=product, user=request.user).exists():
			return Response({'bool': False})
		else:
			WishlistItem.objects.create(product=product, user=request.user)
			return Response({'bool': True})

	@action(detail=False, methods=["get"])
	def my_wishlist(self, request):
		email_or_phone = request.data.get('email_or_phone')
		password = request.query_params.get('password')


		print('---------------------=-=-==-----------------------')
		# print(request.user)
		# print(WishlistItem.objects.all())
		print('---------------------=-=-==-----------------------')
		# print(email_or_phone)
		# print(password)
		# print(request.GET)
		print(request.user.id, '--------1')
		print('---------------------=-=-==-----------------------')


		if request.user.is_authenticated:
			queryset = WishlistItem.objects.filter(user=request.user).order_by('-id')
			serializer = self.get_serializer(queryset, many=True)
			return Response(serializer.data)
		else:
			return Response(
				{"detail": "User is not authenticated"},
				status=status.HTTP_401_UNAUTHORIZED
			)

	'''
	
	GET /wishlist/my-wishlist/?email_or_phone=email@example.com&password=examplepassword
	
	
	def my_wishlist(self, request):
		print('---------------------=-=-==-----------------------')
		print(request.user)
		print(WishlistItem.objects.all())
		print('---------------------=-=-==-----------------------')
		queryset = WishlistItem.objects.filter(user=request.user).order_by('-id')
		print('---------------------=-=-==-----------------------')
		serializer = self.get_serializer(queryset, many=True)
		return Response(serializer.data)'''
'''
 # path('add-wishlist',views.add_wishlist, name='add_wishlist'),
        # path('my-wishlist',views.my_wishlist, name='my_wishlist'),

'''

