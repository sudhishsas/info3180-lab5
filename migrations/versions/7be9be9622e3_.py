"""empty message

Revision ID: 7be9be9622e3
Revises: c88d86f4bec8
Create Date: 2022-03-02 14:31:33.456014

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7be9be9622e3'
down_revision = 'c88d86f4bec8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('password', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profiles', 'password')
    # ### end Alembic commands ###
