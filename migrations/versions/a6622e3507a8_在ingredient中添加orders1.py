"""在ingredient中添加orders1

Revision ID: a6622e3507a8
Revises: bcdce6357073
Create Date: 2023-05-20 20:37:08.151294

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a6622e3507a8'
down_revision = 'bcdce6357073'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_item')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order_item',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('order_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('ingredient_id', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=200), nullable=False),
    sa.ForeignKeyConstraint(['ingredient_id'], ['ingredient.id'], name='order_item_ibfk_2'),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], name='order_item_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
