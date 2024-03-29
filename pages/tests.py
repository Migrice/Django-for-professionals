from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView, AboutPageView

class HomepageTests(SimpleTestCase):

    #Methode appelée avant chaque test
    def setUp(self) -> None:
        url = reverse("home")
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code,  200)

    def test_homepage_url_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'home.html')

    def test_homepage_not_contains_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(response,'Hi there! ')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


class AboutPageTests(SimpleTestCase):
    def setUp(self) -> None:
        url = reverse("about")
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code,  200)

    def test_aboutpage_template(self):
        #response = self.client.get('/about')
        self.assertTemplateUsed(self.response,'about.html')

    def test_about_contains_correct_html(self):
        #response = self.client.get('/about')
        self.assertContains(self.response,'About page')

    def test_aboutpage_not_contains_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(response,'Hi there! ')

    def test_aboutpage_url_resolves_homepageview(self):
        view = resolve("/about/")
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)

