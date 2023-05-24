"""增加role表和user-role关系

Revision ID: e7ae9a0db4f0
Revises: 835045539663
Create Date: 2023-05-19 15:23:11.176855

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e7ae9a0db4f0'
down_revision = '835045539663'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('collection',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('recipe_id', sa.String(length=200), nullable=False),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipe.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('recipe', schema=None) as batch_op:
        batch_op.drop_column('taste')
        batch_op.drop_column('difficulty')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('password', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('active', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('confirmed_at', sa.DateTime(), nullable=True))
        batch_op.create_unique_constraint(None, ['email'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('confirmed_at')
        batch_op.drop_column('active')
        batch_op.drop_column('password')
        batch_op.drop_column('email')

    with op.batch_alter_table('recipe', schema=None) as batch_op:
        batch_op.add_column(sa.Column('difficulty', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=200), nullable=True))
        batch_op.add_column(sa.Column('taste', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=200), nullable=True))

    op.drop_table('collection')
    # ### end Alembic commands ###
