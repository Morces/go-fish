"""Add bio and profile pic columns

Revision ID: a1cad1c1c6d4
Revises: bfb7db1bc143
Create Date: 2022-05-19 01:24:25.819118

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1cad1c1c6d4'
down_revision = 'bfb7db1bc143'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('image_file', sa.String(length=20), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'image_file')
    op.drop_column('users', 'bio')
    # ### end Alembic commands ###
