"""two new fields add in users

Revision ID: a14408e7601e
Revises: 9fda6710085c
Create Date: 2018-07-08 19:41:08.911170

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a14408e7601e'
down_revision = '9fda6710085c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Users', sa.Column('first_name', sa.String(length=50), nullable=False))
    op.add_column('Users', sa.Column('last_name', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Users', 'last_name')
    op.drop_column('Users', 'first_name')
    # ### end Alembic commands ###