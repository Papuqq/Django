from datetime import datetime, timedelta

from django.urls import reverse_lazy

from .models import Post
from .filters import PostFilter
from .forms import PostForm
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.db.models import Exists, OuterRef
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .models import Subscription, Category
from .tasks import hello, printer
from django.http import HttpResponse
from django.views import View

from django.views.decorators.cache import cache_page

@cache_page(60 * 15) # в аргументы к декоратору передаём количество секунд, которые хотим, чтобы страница держалась в кэше. Внимание! Пока страница находится в кэше, изменения, происходящие на ней, учитываться не будут!
def my_view(request):
    ...

class PostCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name = 'product_edit.html'


class PostList(ListView):
    model = Post
    ordering = 'name'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_loaded'] = datetime.now().time()
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'


@login_required
class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('project.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


@login_required
class PostUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('project.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


@login_required
class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('project.delete_post',)
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


@login_required
@csrf_protect
def subscriptions(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        category = Category.objects.get(id=category_id)
        action = request.POST.get('action')

        if action == 'subscribe':
            Subscription.objects.create(user=request.user, category=category)
        elif action == 'unsubscribe':
            Subscription.objects.filter(
                user=request.user,
                category=category,
            ).delete()

    categories_with_subscriptions = Category.objects.annotate(
        user_subscribed=Exists(
            Subscription.objects.filter(
                user=request.user,
                category=OuterRef('pk'),
            )
        )
    ).order_by('name')
    return render(
        request,
        'subscriptions.html',
        {'categories': categories_with_subscriptions},
    )


class IndexView(View):
    def get(self, request):
            printer.apply_async([10],eta=datetime.now() + timedelta(seconds=5))
            hello.delay()
            return HttpResponse('Hello!')
