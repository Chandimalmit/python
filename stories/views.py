from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Story, Rating
from django.db.models import Count


class IndexView(generic.ListView):
    template_name = 'stories/index.html'
    context_object_name = 'all_stories'

    def get_queryset(self):
        return Story.objects.all().order_by('-story_created')[:5]

class DetailView(generic.DetailView):
    model = Story
    template_name = 'stories/detail_form.html'

class CreateStory(CreateView):
    model = Story
    fields = ['story_title', 'story_content']

class RatingView(generic.ListView):
    model = Rating
    fields = ['rating_value', 'story']
    template_name = 'stories/rating.html'
    context_object_name = 'rating_count'

    def get_queryset(self):
        #id = request.POST.get('story_id', "")
        return Rating.objects.all().values('rating_value').annotate(total=Count('rating_value'))

