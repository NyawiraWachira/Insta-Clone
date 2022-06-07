from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm,NewPostForm
from .models import Post, Stream,Profile, Tag, Likes
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here. 

@login_required
def profile(request):

    return render(request, 'profile.html')
    

@login_required
def home(request):
    user=request.user
    posts= Stream.objects.filter(user=user)

    group_ids = []

    for post in posts:
        group_ids.append(post.post_id)
    

    post_items = Post.objects.filter(id__in=group_ids).all().order_by('-posted')

    template=loader.get_template('home.html')

    context= {
        'post_items': post_items,

    }

    return HttpResponse(template.render(context, request  ))    
   

@login_required
def update(request):
    if request.method == 'POST':
            u_form = UserUpdateForm(request.POST, instance=request.user)
            p_form = ProfileUpdateForm(request.POST,
                                    request.FILES,
                                    instance=request.user.profile)
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request, f'Your account has been updated!')
                return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'update.html', context)

def register(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        form = CreateUserForm()
        if request.method =='POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request, "Account Created Successfully! You are now able to log in")

                return redirect('login')


        return render(request, 'authenticate/register.html',{'form':form} )


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        if request.method =='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('profile')

            else:
                messages.info(request, 'Check username or password and try again')

        return render(request, 'authenticate/login.html' )

def logoutUser(request):
    logout(request)

    return redirect('login')


@login_required
def post(request):
	user = request.user.id
	tags_objs = []
	

	if request.method == 'POST':
		form = NewPostForm(request.POST, request.FILES)
		if form.is_valid():
			picture = form.cleaned_data.get('picture')
			caption = form.cleaned_data.get('caption')
			tags_form = form.cleaned_data.get('tags')

			tags_list = list(tags_form.split(','))

			for tag in tags_list:
				t, created = Tag.objects.get_or_create(title=tag)
				tags_objs.append(t)

			p, created = Post.objects.get_or_create(picture=picture, caption=caption, user_id=user)
			p.tags.set(tags_objs) 
			p.save()
			return redirect('home')
	else:
		form = NewPostForm()

	context = {
		'form':form,
	}

	return render(request, 'post.html', context)

def PostDetails(request, post_id):
	post = get_object_or_404(Post, id=post_id)


	template = loader.get_template('post_details.html') 
	
	context = {
		'post':post,	
	}

	return HttpResponse(template.render(context, request))



@login_required
def like(request, post_id):
	user = request.user
	post = Post.objects.get(id=post_id)
	current_likes = post.likes
	liked = Likes.objects.filter(user=user, post=post).count()

	if not liked:
		like = Likes.objects.create(user=user, post=post)
		current_likes = current_likes + 1

	else:
		Likes.objects.filter(user=user, post=post).delete()
		current_likes = current_likes - 1

	post.likes = current_likes
	post.save()

	return HttpResponseRedirect(reverse('home', args=[]))    