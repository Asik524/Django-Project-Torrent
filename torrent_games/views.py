import random

from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from .models import Category, Games, Comment, Profile
from django.views.generic import ListView, DetailView
from .forms import RegisterForm, LoginForm, CommentForm, EditAccountForm, EditProfileForm
from django.contrib import messages
from django.http import FileResponse


# Create your views here.

class GamesListView(ListView):
    model = Games
    template_name = 'tor_games/index.html'
    paginate_by = 12
    context_object_name = 'games'


    extra_context = {
        'title': 'Главная страница: tor_games'
    }


class GamesListByCategory(GamesListView):

    def get_queryset(self):
        games = Games.objects.filter(category_id=self.kwargs['pk'])
        return games

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        category = Category.objects.get(pk=self.kwargs['pk'])
        context['title'] = f'Tor_games: {category.title}'
        return context


class GamesDownload(DetailView):
    model = Games
    template_name = 'tor_games/game_download.html'
    context_object_name = 'game'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        game = Games.objects.get(pk=self.kwargs['pk'])
        game.save()
        games = Games.objects.all()[::-1][:8]
        context['title'] = f'Игра: {game.title}'
        context['games'] = games
        context['comments'] = Comment.objects.filter(game=game)

        if self.request.user.is_authenticated:
            context['form'] = CommentForm()

        profile = Profile.objects.get(user=self.request.user)
        context['profile'] = profile

        random.shuffle(games)


        return context





def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            if user:
                login(request, user)
                messages.success(request, 'Успешный вход в Аккаунт')
                return redirect('index')
            else:
                messages.error(request, 'Не верный логин или пароль')
                return redirect('login')
        else:
            messages.error(request, 'Не верный логин или пароль')
            return redirect('login')

    else:
        login_form = LoginForm()

    context = {
        'title': 'Войти в Аккаунт',
        'login_form': login_form
    }
    return render(request, 'tor_games/login.html', context)


def user_logout(request):
    logout(request)
    messages.warning(request, 'Вы вышли из Аккаунта')
    return redirect('index')


def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user)
            profile.save()
            messages.success(request, 'Регистрация прошла успешно')
            return redirect('login')
        else:
            for field in form.errors:
                messages.error(request, form.errors[field].as_text())
                return redirect('register')

    else:
        form = RegisterForm()

    context = {
        'title': 'Регистрация',
        'form': form
    }

    if not request.user.is_authenticated:
        return render(request, 'tor_games/register.html', context)
    else:
        return redirect('index')


def save_comment(request, pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.game = Games.objects.get(pk=pk)
        comment.user = request.user
        comment.save()
        messages.success(request, 'Ваш комментарий оставлен')
        return redirect('game', pk)


def download_file(request, pk):
    game = Games.objects.get(pk=pk)
    response = FileResponse(open(game.download.path, 'rb'))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment; filename=%s' % game.download.name
    return response


def profile_view(request, pk):
    profile = Profile.objects.get(user_id=pk)

    context = {
        'title': f'Профиль: {request.user.username}',
        'profile': profile,
    }

    return render(request, 'tor_games/profile.html', context)


def edit_account_view(request):
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные Аккаунта изменены')
            return redirect('profile', request.user.pk)
        else:
            for field in form.errors:
                messages.error(request, form.errors[field].as_text())
                return redirect('change')

    else:
        form = EditAccountForm(instance=request.user)

    context = {
        'title': f'Измененние Аккаунта: {request.user.username}',
        'form': form
    }

    return render(request, 'tor_games/change.html', context)


def edit_profile_view(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные Профиля изменены')
            return redirect('profile', request.user.pk)
        else:
            for field in form.errors:
                messages.error(request, form.errors[field].as_text())
                return redirect('change')

    else:
        form = EditProfileForm(instance=request.user.profile)

    context = {
        'title': f'Измененние Профиля: {request.user.username}',
        'form': form
    }

    return render(request, 'tor_games/change.html', context)



