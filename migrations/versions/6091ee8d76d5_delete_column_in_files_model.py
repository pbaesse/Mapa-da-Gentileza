"""delete column in files model

Revision ID: 6091ee8d76d5
Revises: c441fd3f9387
Create Date: 2019-02-07 15:23:25.296482

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6091ee8d76d5'
down_revision = 'c441fd3f9387'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Kindness_Files', 'file_extension')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Kindness_Files', sa.Column('file_extension', mysql.VARCHAR(length=6), nullable=False))
    # ### end Alembic commands ###