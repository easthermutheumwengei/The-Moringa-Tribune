from django.test import TestCase
from .models import  Editor,Article,tags
import datetime as dt

# Create your tests here.
class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.esther=Editor(first_name='esther',last_name='mutheu',email='esthermutheu99@gmail.com')

        def test_instance(self):
            self.assertTrue(isinstance(self.esther,Editor))

# Testing Save Method
def test_save_method(self):
    self.esther.save_editor()
    editors = Editor.objects.all()
    self.assertTrue(len(editors) > 0)

class ArticleTestClass(TestCase):

    def setUp(self):
        #creating a new editor and saving it
        self.esther=Editor(first_name='esther',last_name='mutheu',email='esthermutheu99@gmail.com')
        self.esther.save_editor()

        #creating a new tag and saving it
        self.new_tag=tags(name='testing')
        self.new_tag.save()

        self.new_article=Article(title='Test Article',post='this is a random test post',editor=self.esther)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def test_get_news_today(self):
        todays_news=Article.todays_news()
        self.assertTrue(len(today_news)>0)


    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_by_date(self):
        test_date='2017-03-17'
        date=dt.datetime.strptime(test_date,'%Y-%m-%d').date()
        news_by_date=Article.days_news(date)
        self.assertTrue(len(news_by_date)==0)
