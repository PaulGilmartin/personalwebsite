from collections import namedtuple

# TODO: In this function we store some hard-coded data for the projects,
# since I can't currently find a way to upload a record with long text fields to mysql in the prod db
# To find a way to fix this and eliminate need for hard-coded publication data in this static file
ProjectData = namedtuple('ProjectData', ['content_path', 'abstract', 'coauthors'])

project_title_to_data = {
    'Personal website': ProjectData(coauthors="",
                                    content_path="https://github.com/PaulGilmartin/personalwebsite",
                                    abstract="""This website, built primarily to explore some nice python external
                                                libraries, but also as a way to showcase some of my research work and
                                                pictures. In the backend, it's built primarily using the Python libraries
                                                Flask and SQLAlchemy. In the front-end, I chose to use Jinja2 for
                                                dynamic html template generation and css-bootstrap 
                                                for dynamic visuals""")
}