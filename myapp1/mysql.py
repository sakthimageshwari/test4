'''
from sqlalchemy import create_engine,Column,Integer,String,Date,ForeignKey, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


base=declarative_base()


class Q_A(base):
    __tablename__='Q_A'
    id = Column(Integer, primary_key=True)
    question=Column(String(255),nullable=False)
    option_1=Column(String(255),nullable=False)
    option_2=Column(String(255),nullable=False)
    option_3=Column(String(255),nullable=False)
    option_4=Column(String(255),nullable=False)
    answer=Column(String(255),nullable=False)

class Regform(base):
    __tablename__='Regform'
    id = Column(Integer, primary_key=True)
    fname=Column(String(255),nullable=False)
    lname=Column(String(255),nullable=False)
    gender=Column(String(255),nullable=False)
    dob=Column(Date)
    phone=Column(Integer)
    email=Column(String(255),nullable=False)
    uname=Column(String(255),nullable=False)
    passcode=Column(String(255),nullable=False)

class Q_S(base):
    __tablename__='Q_S'
    id = Column(Integer, primary_key=True)
    question=Column(String(255),nullable=False)
    option_1=Column(String(255),nullable=False)
    option_2=Column(String(255),nullable=False)
    option_3=Column(String(255),nullable=False)
    option_4=Column(String(255),nullable=False)
    answer=Column(String(255),nullable=False)
import os
db_path = os.path.abspath('Library.db')
sqlite_engine = create_engine(f'sqlite:///{db_path}')
#sqlite_engine=create_engine('sqlite:///Library.db') 
mysql_engine = create_engine('mysql+pymysql://root:1234@localhost:3306/testportal')  

SQLite_session= sessionmaker(bind=sqlite_engine)
sqlite_session=SQLite_session()

MYSQL_Session=sessionmaker(bind=mysql_engine)
mysql_session=MYSQL_Session()

base.metadata.create_all(mysql_engine)
for table in[Q_S,Regform,Q_A]:
    records=sqlite_session.query(table).all()
    for record in records:
        mysql_session.merge(record)
mysql_session.commit()

sqlite_session.close()
mysql_session.close()
'''
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# -------------------------------------
# Define SQLAlchemy base and table models
# -------------------------------------
Base = declarative_base()

class Q_A(Base):
    __tablename__ = 'Q_A'
    id = Column(Integer, primary_key=True)
    question = Column(String(255), nullable=False)
    option_1 = Column(String(255), nullable=False)
    option_2 = Column(String(255), nullable=False)
    option_3 = Column(String(255), nullable=False)
    option_4 = Column(String(255), nullable=False)
    answer = Column(String(255), nullable=False)

class Regform(Base):
    __tablename__ = 'Regform'
    id = Column(Integer, primary_key=True)
    fname = Column(String(255), nullable=False)
    lname = Column(String(255), nullable=False)
    gender = Column(String(255), nullable=False)
    dob = Column(Date)
    phone = Column(Integer)
    email = Column(String(255), nullable=False)
    uname = Column(String(255), nullable=False)
    passcode = Column(String(255), nullable=False)

class Q_S(Base):
    __tablename__ = 'Q_S'
    id = Column(Integer, primary_key=True)
    question = Column(String(255), nullable=False)
    option_1 = Column(String(255), nullable=False)
    option_2 = Column(String(255), nullable=False)
    option_3 = Column(String(255), nullable=False)
    option_4 = Column(String(255), nullable=False)
    answer = Column(String(255), nullable=False)

# -------------------------------------
# Resolve the SQLite file path properly
# -------------------------------------
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'Library.db')

if not os.path.exists(db_path):
    raise FileNotFoundError(f"❌ SQLite DB not found at: {db_path}")

# -------------------------------------
# Create engine connections
# -------------------------------------
sqlite_engine = create_engine(f'sqlite:///{db_path}')
mysql_engine = create_engine('mysql+pymysql://root:1234@localhost:3306/testportal1')

# -------------------------------------
# Create session factories
# -------------------------------------
SQLiteSession = sessionmaker(bind=sqlite_engine)
MySQLSession = sessionmaker(bind=mysql_engine)

sqlite_session = SQLiteSession()
mysql_session = MySQLSession()

# -------------------------------------
# Ensure tables exist in MySQL
# -------------------------------------
Base.metadata.create_all(mysql_engine)

# -------------------------------------
# Transfer data with confirmation output
# -------------------------------------
try:
    for table_class in [Q_S, Regform, Q_A]:
        records = sqlite_session.query(table_class).all()
        print(f"📦 Transferring {len(records)} rows from {table_class.__tablename__}...")
        for record in records:
            mysql_session.merge(record)
    mysql_session.commit()
    print("✅ Data migrated successfully to MySQL!")

except Exception as e:
    print("❌ Migration failed:", e)

finally:
    sqlite_session.close()
    mysql_session.close()