"""empty message

Revision ID: 22e0ce6e61de
Revises: 46d4b157d052
Create Date: 2018-09-09 18:16:17.982953

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22e0ce6e61de'
down_revision = '46d4b157d052'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('card', sa.Column('days_till', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('card', 'days_till')
    # ### end Alembic commands ###
