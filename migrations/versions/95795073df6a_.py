"""empty message

Revision ID: 95795073df6a
Revises: 222724339795
Create Date: 2020-07-06 16:56:43.316558

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95795073df6a'
down_revision = '222724339795'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('shows_venue_id2_fkey', 'shows', type_='foreignkey')
    op.drop_column('shows', 'venue_id2')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shows', sa.Column('venue_id2', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('shows_venue_id2_fkey', 'shows', 'venues', ['venue_id2'], ['id'])
    # ### end Alembic commands ###
