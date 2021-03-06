"""table created

Revision ID: 6427360b0479
Revises: 
Create Date: 2021-04-13 20:08:29.566763

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6427360b0479'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('barber_shop',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=False),
    sa.Column('phone_number', sa.String(length=15), nullable=False),
    sa.Column('cnpj', sa.String(length=14), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=120), nullable=False),
    sa.Column('user_type', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cnpj'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('phone_number')
    )
    op.create_table('client',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=False),
    sa.Column('phone_number', sa.String(length=15), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=120), nullable=False),
    sa.Column('user_type', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone_number')
    )
    op.create_table('address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('barber_shop_name', sa.String(length=40), nullable=False),
    sa.Column('state', sa.String(length=40), nullable=False),
    sa.Column('city', sa.String(length=40), nullable=False),
    sa.Column('street_name', sa.String(length=40), nullable=False),
    sa.Column('building_number', sa.String(length=20), nullable=False),
    sa.Column('zip_code', sa.String(length=20), nullable=False),
    sa.ForeignKeyConstraint(['barber_shop_name'], ['barber_shop.name'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('barber_shop_name')
    )
    op.create_table('barbers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('barber_shop_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=40), nullable=False),
    sa.Column('user_type', sa.String(length=30), nullable=False),
    sa.ForeignKeyConstraint(['barber_shop_id'], ['barber_shop.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('services',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('service_name', sa.String(length=40), nullable=False),
    sa.Column('service_price', sa.String(length=4), nullable=False),
    sa.Column('barber_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['barber_id'], ['barbers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('appointments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('barber_id', sa.Integer(), nullable=False),
    sa.Column('barber_shop_id', sa.Integer(), nullable=False),
    sa.Column('services_id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('date_time', sa.String(length=20), nullable=False),
    sa.ForeignKeyConstraint(['barber_id'], ['barbers.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['barber_shop_id'], ['barber_shop.id'], ),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['services_id'], ['services.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('appointments')
    op.drop_table('services')
    op.drop_table('barbers')
    op.drop_table('address')
    op.drop_table('client')
    op.drop_table('barber_shop')
    # ### end Alembic commands ###
