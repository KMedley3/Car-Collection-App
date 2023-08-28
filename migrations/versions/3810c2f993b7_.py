"""empty message

Revision ID: 3810c2f993b7
Revises: d4b7026a302e
Create Date: 2023-08-21 18:17:51.540403

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3810c2f993b7'
down_revision = 'd4b7026a302e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('car',
    sa.Column('make', sa.String(), nullable=False),
    sa.Column('model', sa.String(length=150), nullable=False),
    sa.Column('year', sa.String(length=200), nullable=True),
    sa.Column('color', sa.String(length=20), nullable=True),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('make')
    )
    op.drop_table('contact')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contact',
    sa.Column('id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('phone_number', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('address', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('user_token', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], name='contact_user_token_fkey'),
    sa.PrimaryKeyConstraint('id', name='contact_pkey')
    )
    op.drop_table('car')
    # ### end Alembic commands ###