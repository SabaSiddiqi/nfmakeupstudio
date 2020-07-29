
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .forms import ContactForm

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import coverPhoto,portfolioPhoto_henna, portfolioPhoto_makeup,portfolioPhoto_hairdo,html_info
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings
from django.core.mail import EmailMessage


def mainpage(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            print('Form is valid')
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            print(name,subject,from_email,message)

            msg = "Email : " + from_email + "\n" + "Name : " + name + "\n" + "Message : " + message + "\n"

            try:
                send_mail( subject, msg , 'saba.siddiqui.2010@gmail.com', ['saba.siddiqui.2010@gmail.com'],fail_silently=False)
            except BadHeaderError:
                 return HttpResponse('Invalid header found.')
    context={'cover': coverPhoto.objects.all(), 'portfolio_makeup':portfolioPhoto_makeup.objects.all(), 'contactform': form, 'portfolio_hairdo': portfolioPhoto_hairdo.objects.all(),'portfolio_henna':portfolioPhoto_henna.objects.all()}
    #return HttpResponse('successfully uploaded')
    return render(request, 'myapp/index.html',context)

def homepage(request):
    #context={'index': CatIndex.objects.all(), 'blog': Post.objects.all()}
    #return HttpResponse('successfully uploaded')
    return render(request, 'myapp/home.html')

def image_app_page(request):
    #context={'index': CatIndex.objects.all(), 'blog': Post.objects.all()}
    #return HttpResponse('successfully uploaded')
    return render(request, 'myapp/image_app.html')



# Create your views here.
def hotel_image_view(request):

    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = HotelForm()
    return render(request, 'hotel_image_form.html', {'form' : form})


def success(request):
    return HttpResponse('successfully uploaded')


def send_values(request):
    # print("I'm here")
    # x=["0","60"]
    # if request.method == 'POST':
    #     print("I'm here TOO")
    #     x = "500"
    x = ["hello world"]
    return render(request, 'myapp/zucov-cdvw9.html', {'x':x})

from io import StringIO,BytesIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from cgi import escape


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = BytesIO()

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

def save_pdf(request):
    x={}
    # dictionary with integer keys
    x={'pagesize':'A4','mylist': 'ball'}
    return render_to_pdf('myapp/zucov-cdvw9.html',{'pagesize':'A4','mylist': 'ball'})
    #
    # send_values(request)
    # import pdfkit
    # path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
    # config = pdfkit.configuration(wkhtmltopdf = path_wkthmltopdf)
    # pdfkit.from_url("http://127.0.0.1:8000/home/html", "out.pdf", configuration=config)
    # return render_to_pdf (request, 'myapp/zucov-cdvw9.html', {'x':x})
        #     'mytemplate.html',
        #     {
        #         'pagesize':'A4',
        #         'mylist': results,
        #     }
        # )
