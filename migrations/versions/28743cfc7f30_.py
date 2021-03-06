"""empty message

Revision ID: 28743cfc7f30
Revises: 
Create Date: 2022-05-23 13:40:42.428331

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28743cfc7f30'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_name', sa.String(length=20), nullable=True),
    sa.Column('parent_name', sa.String(length=20), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('phone', sa.String(length=120), nullable=True),
    sa.Column('address', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_student_address'), 'student', ['address'], unique=False)
    op.create_index(op.f('ix_student_email'), 'student', ['email'], unique=False)
    op.create_index(op.f('ix_student_parent_name'), 'student', ['parent_name'], unique=False)
    op.create_index(op.f('ix_student_phone'), 'student', ['phone'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_student_phone'), table_name='student')
    op.drop_index(op.f('ix_student_parent_name'), table_name='student')
    op.drop_index(op.f('ix_student_email'), table_name='student')
    op.drop_index(op.f('ix_student_address'), table_name='student')
    op.drop_table('student')
    # ### end Alembic commands ###
