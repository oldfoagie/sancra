from django.shortcuts import render
from django.utils import timezone
from .models import Post

from django.template import RequestContext
from django.shortcuts import render_to_response
#from web.forms import codeUploadForm
#from web.csvTools import CodeCSvModel


# Create your views here.
def post_list(request):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def home(request):
    return render(request, 'blog/home.html')

def board(request):
    return render(request, 'blog/board.html')

def cities(request):
    return render(request, 'blog/cities.html')

def orgs(request):
    return render(request, 'blog/orgs.html')


def codeImport(request):
    # If we had a POST then get the request post values.

    if request.method == 'POST':
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['html-file-attribute-name']

            # Write the file to disk
            fout = open("path/to/save/file/to/%s" % uploaded_file.name, 'wb')
            for chunk in uploaded_file.chunks():
                fout.write(chunk)
            fout.close()

    #        CodeCSvModel.import_from_file(form['file'])



        else:
             form = codeUploadForm()
             context = {'form':form}
             return render_to_response('import.html', context, context_instance=RequestContext(request))
