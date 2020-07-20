"""empty message

Revision ID: daad5035de40
Revises: 95795073df6a
Create Date: 2020-07-06 17:02:08.239829

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'daad5035de40'
down_revision = '95795073df6a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shows', sa.Column('venue_id2', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'shows', 'venues', ['venue_id2'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'shows', type_='foreignkey')
    op.drop_column('shows', 'venue_id2')
    # ### end Alembic commands ###