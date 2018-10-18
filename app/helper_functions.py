from app import create_app, db
from app.main.models import Paper, Photograph, Painting, Project
from config import Config


class_map = {cls.__name__: cls for cls in (Paper, Photograph, Painting, Project)}


def app_context(config_class=Config):
    app = create_app(config_class)
    return app.app_context()


def create_model_item(class_name, **kwargs):
    with app_context():
        item = class_map[class_name](**kwargs)
    return item


def commit_item(item, database=None, config_class=Config):
    with app_context(config_class):
        database = database or db
        database.session.add(item)
        database.session.commit()


def get_all_items_of_type(model_name, config_class=Config):
    with app_context(config_class):
        model_cls = class_map[model_name]
        all_items = model_cls.query.all()
    return all_items


def delete_item(item, database=None, config_class=Config):
    with app_context(config_class):
        database = database or db
        database.session.delete(item)
        database.session.commit()


def build_records(database=None, config_class=Config):
    with app_context(config_class):
        database = database or db

        kgPhoto = create_model_item('Photograph', content_path='../static/kelvinbridgePhotograph.JPG',
                                    title='Kelvinbridge', subject='Glasgow')
        kgPainting = create_model_item('Painting', content_path='../static/kelvinBridgePainting.png',
                                       title='Kelvinbridge', subject='Glasgow', photograph=kgPhoto)

        wPhoto = create_model_item('Photograph', content_path='../static/westPrincesStreetPhotograph.JPG',
                                   title='West Princes Street', subject='Glasgow')
        wPainting = create_model_item('Painting', content_path='../static/westPrincesStreetPainting.png',
                                      title='West Princes Street', subject='Glasgow', photograph=wPhoto)

        for i in [kgPhoto, kgPainting, wPhoto, wPainting]:
            commit_item(i)
