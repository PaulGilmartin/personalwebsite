from app.main import bp as main_bp
from app.main.models import Painting, Paper, Photograph, Project
from app.static.publications_config import publications_title_to_data
from flask import render_template, url_for

from collections import namedtuple

Link = namedtuple('Link', ['link', 'display'])


@main_bp.route('/')
@main_bp.route('/home')
def home():
    links = [Link(link='main.projects', display='Projects'), Link('main.publications', display='Publications'),
             Link(link='main.gallery_front', display='Gallery')]
    return render_template('home.html', links=links, central_image="static/anderstonFootbridge.jpg")


@main_bp.route('/about')
def about():
    local_links = [Link(link='main.about', display='C.V.'),
                   Link(link='main.projects', display='Projects')]
    web_links = [Link(link='https://www.linkedin.com/in/paul-gilmartin/', display='LinkedIn')]
    return render_template('about.html', local_links=local_links, web_links=web_links)


@main_bp.route('/contact')
def contact():
    return render_template('contact.html')


@main_bp.route('/publications')
def publications():
    papers = Paper.query.all()
    blurb = """My research interests lie primarily in the field of non-commutative algebra. I'm particularly interested in
             Hopf algebras of finite GK-dimension, quantum groups, quantum homogeneous spaces
             and Poisson algebraic groups. My published research papers in this field are listed below."""

    # TODO: in the below we pass a paper_config variable in to avoid having to include long text data
    # since I can't currently find a way to upload a record with such properties to mysql in the prod db
    # To find a way to fix this and eliminate need for hard-coded publication data in the static file
    return render_template('/publications.html', blurb=blurb, papers=papers,
                           paper_config=publications_title_to_data, title='Publications')


@main_bp.route('/projects')
def projects():
    projs = Project.query.all()
    blurb = """This page details some of the programming projects I've worked on in my spare time. More to come
    in the not too distant future."""
    return render_template('/projects.html', papers=projs, blurb=blurb, title='Projects')


@main_bp.route('/gallery')
def gallery_front():
    links = [Link('main.glasgow', display='Glasgow'), Link(link='main.pubs', display='Pubs'),
             Link(link='main.paintings', display='Paintings')]
    return render_template('/gallery/gallery_front.html', links=links,
                           central_image="../static/maryhill.jpg")


@main_bp.route('/gallery/pubs')
def pubs():
    photos = Photograph.query.filter_by(subject='Pub').all()
    return render_template('/gallery/pubs.html', photos=photos, title='Pubs')


@main_bp.route('/gallery/glasgow')
def glasgow():
    photos = Photograph.query.filter_by(subject='Glasgow').all()
    return render_template('/gallery/glasgow.html', photos=photos, title='Glasgow')


@main_bp.route('/gallery/paintings')
def paintings():
    paintings = Painting.query.all()
    return render_template('/gallery/paintings.html', photos=paintings, title='Paintings')

