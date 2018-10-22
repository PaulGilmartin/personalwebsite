from app import db


class MediaMixin(object):

    def __repr__(self):
        return '<{} {}>'.format(self.__class__.__name__, self.title)


class Paper(MediaMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    content_path = db.Column(db.Text)
    title = db.Column(db.Text, index=True)
    abstract = db.Column(db.Text)
    coauthors = db.Column(db.Text, index=True)


class Project(MediaMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    content_path = db.Column(db.Text)
    title = db.Column(db.Text, index=True)
    abstract = db.Column(db.Text())
    coauthors = db.Column(db.Text(), index=True)


class Photograph(MediaMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    content_path = db.Column(db.String(64))
    title = db.Column(db.String(64), index=True)
    subject = db.Column(db.String(64), index=True)  # e.g. 'Pub' or 'Glasgow'
    painting = db.relationship('Painting', backref='photograph', lazy='dynamic')

    def modal_images(self):
        """
        The images which dynamically appear when we click on the base image
        """
        return [self.content_path]


class Painting(MediaMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    content_path = db.Column(db.String(64))
    title = db.Column(db.String(64), index=True)
    subject = db.Column(db.String(64), index=True)
    photo_id = db.Column(db.Integer, db.ForeignKey('photograph.id'))

    def modal_images(self):
        """
        The images which dynamically appear when we click on the base image
        """
        return [self.content_path, self.photograph.content_path]
