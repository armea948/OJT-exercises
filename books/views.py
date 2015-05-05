from django.shortcuts import render, redirect
from books.models import Book, Author, Publisher
from books.forms import ContactForm, SignUp, AuthorForm, PublisherForm, BookForm, LoginForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def search(request):
    errors = [] #False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request,
                'search_results.html',
                {'books': books, 'query': q},
                )
    return render(request, 'search_form.html', {'error': errors})

def contact(request):
        if request.method == 'POST':  # If the form has been submitted...
                form = ContactForm(request.POST)  # A form bound to the POST data
                if form.is_valid():
                        subject = form.cleaned_data['subject']
                        message= form.cleaned_data['message']
                        sender = form.cleaned_data['sender']
                        cc_myself = form.cleaned_data['cc_myself']
                        recipients = ['kdlim948@yahoo.com']
                        if cc_myself:
                            recipients.append(sender)
                        return HttpResponse('Thanks')
        else:
                form = ContactForm()  # An unbound form

        return render(
                request,
                'contact.html',
                {'form': form}
        )

def signUp(request):
    error = None
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeatpwd = form.cleaned_data['repeatpwd']
            if password == repeatpwd:
                new_user = User.objects.create_user(
                    username=username,
                    password=password,
                    email=email
                    )
                new_user.first_name = first_name
                new_user.last_name = last_name
                new_user.save()
                return HttpResponse('User Added')
            else:
                error ="Password does not match"
                return render(request, 'signup.html', {'form': form, 'error': error})
    else:
        form = SignUp()
    return render(request, 'signup.html', {'form': form, 'error': error})

def addAuthor(request):
    new_author = Author()
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']

            new_author.first_name = first_name
            new_author.last_name = last_name
            new_author.email = email
            new_author.age = age
            new_author.save()

            #return HttpResponse("Author Added")
            #return render(request, 'auth_users.html')
            return redirect('/books/home/')
    else:
        form = AuthorForm()
    return render(request, 'author.html', {'form': form})

def addPublisher(request):
    new_publisher = Publisher()
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            state_province = form.cleaned_data['state_province']
            country = form.cleaned_data['country']
            website = form.cleaned_data['website']
            phone = form.cleaned_data['phone']

            new_publisher.name = name
            new_publisher.address = address
            new_publisher.city = city
            new_publisher.state_province = state_province
            new_publisher.country = country
            new_publisher.website = website
            new_publisher.phone = phone
            new_publisher.save()

            #return HttpResponse("Publisher Added")
            #return render(request, 'auth_users.html')
            return redirect('/books/home/')
    else:
        form = PublisherForm()
    return render(request, 'publisher.html', {'form': form})

def addBook(request):
        if request.method == 'POST':
            form = BookForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                authors = form.cleaned_data['authors']
                publisher = form.cleaned_data['publisher']
                publication_date = form.cleaned_data['publication_date']
                description = form.cleaned_data['description']
                new_book = Book(title=title,
                    publisher=publisher,
                    publication_date=publication_date,
                    description=description)
                new_book.save()
                for i in range(0,len(authors)):
                    new_book.authors.add(authors[i])
                new_book.save()
                #return HttpResponse("You have added a New Book.")
                #return render(request, 'auth_users.html')
                return redirect('/books/home/')
        else:
            form = BookForm()
        return render(request,'book.html',{'form':form})

def home(request):
    return render(request, 'auth_users.html')

def my_view(request):
    #logout(request)
    #if(request)
    if request.user.is_authenticated():
        return redirect('/books/home/')
    else:
        message = None
        if request.method == 'POST':

            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            print user
            form = LoginForm(request.POST)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    message = "Success"
                    #return HttpResponseRedirect('/admin/')
                    #return render(request, 'auth_users.html')
                    return redirect('/books/home/')

                else:
                    message = "Account disabled"
            else:
                message = "Login invalid"
        else:
                form = LoginForm()
        return render(request, 'login.html', {'form': form, 'message': message})

def logout_view(request):
    logout(request)
    return redirect('/books/login')
    #form = LoginForm()

    #return render(request, 'login.html', {'form': form})
