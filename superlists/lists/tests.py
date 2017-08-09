from django.core.urlresolvers import resolve
from django.test import TestCase
from .views import home_page
#from ..lists.views import home_page
#from superlists.lists.views import home_page #1

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/') #2
        self.assertEqual(found.func, home_page)