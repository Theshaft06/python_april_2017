from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'landscapes_app.index.html')

def show(request, id):
	landscape = ''
	if id > 0 and id < 10:
		landscape = 'http://www.qygjxz.com/data/out/209/4791077-snow-pictures.jpg'
	elif id > 9 and id < 20:
		landscape = 'https://images.pexels.com/photos/3853/sunny-sand-desert-hiking.jpeg?h=350&auto=compress&cs=tinysrgb'
	elif id > 19 and id < 30:
		landscape = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQBjghk0J6Z_n5qD6_8_2ogoiZHtejq9j3J5LbLBCKlANDGISqx'
	elif id > 29 and id < 40:
		landscape = 'http://www.terlatovineyards.com/sites/default/files/slideshow/vineyard-grapes-home-slideshow.jpg'
	else: 
		landscape = 'http://world-visits.com/wp-content/uploads/2012/02/Tropical-Island-6.jpg'

	context = {
		landscape: landscape
	}

	return render(request, 'landscapes_app.show.html', context)