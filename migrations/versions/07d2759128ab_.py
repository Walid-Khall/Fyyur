"""empty message

Revision ID: 07d2759128ab
Revises: fb64e1ce9191
Create Date: 2020-07-09 11:45:40.826563

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07d2759128ab'
down_revision = 'fb64e1ce9191'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shows', sa.Column('artist_image_link', sa.String(length=500), nullable=True))
    op.add_column('shows', sa.Column('artist_name', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('shows', 'artist_name')
    op.drop_column('shows', 'artist_image_link')
    # ### end Alembic commands ###
