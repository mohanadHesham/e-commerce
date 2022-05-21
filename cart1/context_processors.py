from cart1 import Cart

def cart(request):
	return {'cart':Cart(request)}