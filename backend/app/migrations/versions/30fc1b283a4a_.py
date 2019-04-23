"""empty message

Revision ID: 30fc1b283a4a
Revises: 851906bbe1e0
Create Date: 2019-04-23 20:39:33.132490

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30fc1b283a4a'
down_revision = '851906bbe1e0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogposts', sa.Column('header_img', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blogposts', 'header_img')
    # ### end Alembic commands ###