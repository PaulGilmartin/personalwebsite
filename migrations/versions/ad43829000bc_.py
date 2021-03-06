"""empty message

Revision ID: ad43829000bc
Revises: 
Create Date: 2018-10-22 21:54:45.934639

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad43829000bc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('paper',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content_path', sa.Text(), nullable=True),
    sa.Column('title', sa.Text(), nullable=True),
    sa.Column('abstract', sa.Text(), nullable=True),
    sa.Column('coauthors', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_paper_coauthors'), 'paper', ['coauthors'], unique=False)
    op.create_index(op.f('ix_paper_title'), 'paper', ['title'], unique=False)
    op.create_table('photograph',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content_path', sa.String(length=64), nullable=True),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('subject', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_photograph_subject'), 'photograph', ['subject'], unique=False)
    op.create_index(op.f('ix_photograph_title'), 'photograph', ['title'], unique=False)
    op.create_table('project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content_path', sa.Text(), nullable=True),
    sa.Column('title', sa.Text(), nullable=True),
    sa.Column('abstract', sa.Text(), nullable=True),
    sa.Column('coauthors', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_project_coauthors'), 'project', ['coauthors'], unique=False)
    op.create_index(op.f('ix_project_title'), 'project', ['title'], unique=False)
    op.create_table('painting',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content_path', sa.String(length=64), nullable=True),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('subject', sa.String(length=64), nullable=True),
    sa.Column('photo_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['photo_id'], ['photograph.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_painting_subject'), 'painting', ['subject'], unique=False)
    op.create_index(op.f('ix_painting_title'), 'painting', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_painting_title'), table_name='painting')
    op.drop_index(op.f('ix_painting_subject'), table_name='painting')
    op.drop_table('painting')
    op.drop_index(op.f('ix_project_title'), table_name='project')
    op.drop_index(op.f('ix_project_coauthors'), table_name='project')
    op.drop_table('project')
    op.drop_index(op.f('ix_photograph_title'), table_name='photograph')
    op.drop_index(op.f('ix_photograph_subject'), table_name='photograph')
    op.drop_table('photograph')
    op.drop_index(op.f('ix_paper_title'), table_name='paper')
    op.drop_index(op.f('ix_paper_coauthors'), table_name='paper')
    op.drop_table('paper')
    # ### end Alembic commands ###
