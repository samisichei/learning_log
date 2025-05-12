from django.shortcuts import redirect, render
from django.contrib.auth import logout, login, authenticate
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def logout_view(request):
    """log the user out."""
    logout(request)
    return redirect(reverse('learning_logs:index'))

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form
        form = UserCreationForm()
    else:
        # Process completed form
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password1']
            authenticated_user = authenticate(username=username, password=raw_password)
            login(request, authenticated_user)
            return redirect('learning_logs:index')  # Redirect to your blog home page

    context = {'form': form}
    return render(request, 'users/register.html', context)
