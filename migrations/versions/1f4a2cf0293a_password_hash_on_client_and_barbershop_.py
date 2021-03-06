"""password hash on client and barbershop models

Revision ID: 1f4a2cf0293a
Revises: 9953f5a313e2
Create Date: 2021-04-16 11:19:07.324316

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f4a2cf0293a'
down_revision = '9953f5a313e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('barber_shop', sa.Column('password_hash', sa.String(), nullable=False))
    op.drop_column('barber_shop', 'password')
    op.add_column('client', sa.Column('password_hash', sa.String(), nullable=False))
    op.drop_column('client', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('client', sa.Column('password', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
    op.drop_column('client', 'password_hash')
    op.add_column('barber_shop', sa.Column('password', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
    op.drop_column('barber_shop', 'password_hash')
    # ### end Alembic commands ###
