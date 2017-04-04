"""empty message

Revision ID: 98dcaf3c762a
Revises: ff2fdfbe648f
Create Date: 2017-03-31 23:10:02.524636

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '98dcaf3c762a'
down_revision = 'ff2fdfbe648f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', mysql.VARCHAR(length=50), nullable=False))
    # ### end Alembic commands ###
