from app import create_app, db
from app.main.models import Paper, Painting, Photograph
from config import Config
import unittest


# create test config which sets up an in memory db so as not to interfere with out prod db
class TestConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class MediaModelTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_paper_model(self):
        paper = Paper(content_path='www.paper.com', title='Maths',
                      abstract='a maths paper', coauthors='Ken')
        db.session.add(paper)
        db.session.commit()
        self.assertEqual(Paper.query.all(), [paper])

    def test_create_photograph_model(self):
        pub_photo = Photograph(content_path='static/photo', title='my pub photo',
                               subject='pub')
        db.session.add(pub_photo)
        db.session.commit()
        self.assertEqual(Photograph.query.all(), [pub_photo])

        shop_photo = Photograph(id=2, content_path='static/photo', title='my shop photo',
                                subject='shop')
        db.session.add(shop_photo)
        db.session.commit()
        self.assertEqual(Photograph.query.all(), [pub_photo, shop_photo])
        result = Photograph.query.filter_by(subject='pub').all()
        self.assertEqual(result, [pub_photo])

    def test_media_type_query(self):
        paper = Paper(content_path='www.paper.com', title='Maths',
                      abstract='a maths paper', coauthors='Ken')
        db.session.add(paper)
        db.session.commit()
        pub_photo = Photograph(content_path='static/photo', title='my pub photo',
                               subject='pub',)
        db.session.add(pub_photo)
        db.session.commit()
        result = Paper.query.all()
        self.assertEqual(result, [paper])

    def test_paper_painting_relationship(self):

        pub_photo = Photograph(content_path='static/photo', title='my pub photo',
                               subject='pub')

        pub_painting = Painting(content_path='static/painting', title='my pub photo',
                                subject='pub', photograph=pub_photo)
        db.session.add(pub_photo)
        db.session.add(pub_painting)
        db.session.commit()

        painting = Painting.query.all()[0]
        self.assertEqual(painting.photograph, pub_photo)
