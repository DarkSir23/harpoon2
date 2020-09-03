from __future__ import unicode_literals

from django.conf.urls import url

# from watson.views import search, search_json
from watson.views import SearchView

def search(request, **kwargs):
    """Renders a page of search results."""
    return NewSearchView.as_view(**kwargs)(request)


app_name = 'watson'
urlpatterns = [

    url("^$", search, name="search"),
#    url("^json/$", search_json, name="search_json"),

]


class NewSearchView(SearchView):

    """View that performs a search and returns the search results."""

    template_name = "search_results.html"
