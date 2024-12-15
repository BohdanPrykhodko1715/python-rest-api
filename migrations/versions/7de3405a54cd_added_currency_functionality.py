"""added currency functionality

Revision ID: 7de3405a54cd
Revises: 089db15cd93e
Create Date: 2024-12-15 16:29:41.078158

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7de3405a54cd'
down_revision = '089db15cd93e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('currencies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=10), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code')
    )
    with op.batch_alter_table('records', schema=None) as batch_op:
        batch_op.add_column(sa.Column('currency_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'currencies', ['currency_id'], ['id'])

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('default_currency_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'currencies', ['default_currency_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('default_currency_id')

    with op.batch_alter_table('records', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('currency_id')

    op.drop_table('currencies')
    # ### end Alembic commands ###