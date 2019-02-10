from django.shortcuts import render

# Create your views here.
def First_view(request):
	context ={
	'msg' : "Hello World!"
	}
	return render(request, "test.html", context)
