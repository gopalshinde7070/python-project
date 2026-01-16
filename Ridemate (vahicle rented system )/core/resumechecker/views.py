from django.shortcuts import render,redirect

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import JobDescriptionSerializers,JobDescription,ResumeSerializer,Resume
from .anaylizer import process_resume


from .models import RegisterUser
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

def admin_job(request):
    if request.method == "POST":
        job_title = request.POST.get("job_title")
        job_description = request.POST.get("job_description")

        JobDescription.objects.create(job_title=job_title, job_description=job_description )

        return redirect("admin_job")

    return render(request, "admin_job.html")

@login_required
def admin_job_list(request):
    jobs = JobDescription.objects.all().order_by("-id")
    return render(request, "admin_job_list.html", {"jobs": jobs})



@login_required
def edit_job(request, id):
    job = JobDescription.objects.get(id=id)

    if request.method == "POST":
        job.job_title = request.POST.get("job_title")
        job.job_description = request.POST.get("job_description")
        job.save()
        return redirect("admin_job_list")

    return render(request, "edit_job.html", {"job": job})

@login_required
def delete_job(request, id):
    job = JobDescription.objects.get(id=id)
    job.delete()
    return redirect("admin_job_list")


def all_admin_side_matterial(request):
    return render(request,'all_admin_side_matterial.html')

def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            login(request, user)   # 🔥 Django session created
            return redirect('all_admin_side_matterial')
        else:
            return render(request, 'admin_login.html', {
                'error': 'Invalid admin credentials'
            })

    return render(request, 'admin_login.html')

def homepage(request):
    return render(request,'homepage.html')

from .models import RegisterUser

from django.shortcuts import render, redirect
from .models import RegisterUser

def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # 🔒 password match check
        if password != confirm_password:
            return render(request, 'register.html', {
                'error': 'Passwords do not match'
            })

        # 🚫 username already exists
def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # 🔒 password match
        if password != confirm_password:
            return render(request, 'register.html', {
                'error': 'Passwords do not match'
            })

        # 🚫 username exists
        if RegisterUser.objects.filter(username=username).exists():
            return render(request, 'register.html', {
                'error': 'Username already exists'
            })

        # 🚫 email exists
        if RegisterUser.objects.filter(email=email).exists():
            return render(request, 'register.html', {
                'error': 'Email already registered'
            })

        RegisterUser.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            phone=phone,
            password=password   # ⚠️ hashing later
        )

        return redirect('login')

    return render(request, 'register.html')

    



from django.contrib.auth import authenticate, login

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)

            return redirect('index')

        return render(request, 'login.html', {
            'error': 'Invalid credentials'
        })

    return render(request, 'login.html')

def user_logout(request):
    logout(request)   # 🔥 clears session & auth
    return redirect('homepage')  # or 'login'

def ht(request):
    return render(request,'ht.html')

@login_required
def index(request):
    return render(request, "index.html")

class JobDescriptionAPI(APIView):
    def get(self,request):
        queryset=JobDescription.objects.all()
        serializer=JobDescriptionSerializers(queryset,many=True)
        return Response({
            'status':True,
            'data':serializer.data,
        })
    
    
class AnalyzeResumeAPI(APIView):
    def post(self, request):
        try:
            data = request.data

            if not data.get('job_description'):
                return Response({
                    'status': False,
                    'message': 'job_description is required',
                })

            serializer = ResumeSerializer(data=data)
            if not serializer.is_valid():
                return Response({
                    'status': False,
                    'errors': serializer.errors
                })

            serializer.save()

            resume_instance = Resume.objects.get(id=serializer.data['id'])
            resume_path = resume_instance.resume.path

            job = JobDescription.objects.get(id=data.get('job_description'))

            result = process_resume(resume_path, job.job_description)

            return Response({
                'status': True,
                'message': 'resume analyzed',
                'data': result
            })

        except Exception as e:
            print("ERROR:", e)  # terminal output
            return Response({
                'status': False,
                'error': str(e)
            })

            
