from django.shortcuts import render

def welcome_view(request):
    user_name = "John Doe"  # Replace with dynamic data or logic to fetch the user's name
    context = {
        'name': user_name,
    }
    return render(request, 'welcome.html', context)
