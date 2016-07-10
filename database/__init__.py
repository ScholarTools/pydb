# Standard imports
import os

# Third party imports
import sqlalchemy as sql
from sqlalchemy.orm import sessionmaker

# Local imports
from database import db_tables as tables


# These database functions can be called from a number of
# different repos. Without specifying an absolute path, a
# new database file would be created in the root directories
# of each repo that uses a Session() object.
# This method strips the filepath down to ScholarTools and
# then points it to create a papers.db file within pydb.

package_path = os.path.dirname(os.path.realpath(__file__))

db_path = os.path.join(package_path,'papers.db')

#path_parts = os.path.split(package_path)
#while path_parts[1] != 'ScholarTools':
#    path_parts = os.path.split(path_parts[0])

dialect = 'sqlite:///'
#path = path_parts[0] + '/ScholarTools/pydb/database/papers.db'

# Combine the dialect and path names to use as params for the engine
engine_params = dialect + db_path

engine = sql.create_engine(engine_params, echo=False)
tables.Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

