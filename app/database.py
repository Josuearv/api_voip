import sqlalchemy as sa
from sqlalchemy.orm import Session

engine = sa.create_engine("mysql+pymysql://root:password@localhost/mbilling")

Session = sa.orm.sessionmaker(bind=engine)
