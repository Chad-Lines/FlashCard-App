"""card table

Revision ID: 80168d6ca60a
Revises: 5465009a359c
Create Date: 2018-09-05 11:32:40.779743

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80168d6ca60a'
down_revision = '5465009a359c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('card',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('front', sa.String(length=1000), nullable=True),
    sa.Column('back', sa.String(length=1000), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_card_timestamp'), 'card', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_card_timestamp'), table_name='card')
    op.drop_table('card')
    # ### end Alembic commands ###
