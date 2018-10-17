from app import create_app, db
from app.main.models import Photograph, Paper, Painting

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Paper': Paper, 'Photograph': Photograph, 'Painting': Painting}