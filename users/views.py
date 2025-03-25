# from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    # redirect_authenticated_user = True  # Redirects if user is already logged in

    # def get_success_url(self):
    #     return reverse_lazy('/')  # Redirects to home page after login


class CustomLogoutView(LogoutView):

    def dispatch(self, request, *args, **kwargs):
        super().dispatch(request, *args, **kwargs)
        return redirect('/')
