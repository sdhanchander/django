from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import UserDetails

# Get all users
def get_all_users(request):
    if request.method == 'GET':
        users = list(UserDetails.objects.values())
        return JsonResponse(users, safe=False)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

# Get a user by email
def get_user_by_email(request, email):
    if request.method == 'GET':
        user = get_object_or_404(UserDetails, email=email)
        return JsonResponse({
            'username': user.username,
            'email': user.email,
            'password': user.password,
        })
    return JsonResponse({'error': 'Invalid request method'}, status=405)

# Update a user by email
def update_user(request, email):
    if request.method == 'POST':
        user = get_object_or_404(UserDetails, email=email)
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username:
            user.username = username
        if password:
            user.password = password
        user.save()
        return JsonResponse({'status': 'User updated'})
    return JsonResponse({'error': 'Invalid request method'}, status=405)

# Delete a user by email
def delete_user(request, email):
    if request.method == 'DELETE':
        user = get_object_or_404(UserDetails, email=email)
        user.delete()
        return JsonResponse({'status': 'User deleted'})
    return JsonResponse({'error': 'Invalid request method'}, status=405)
