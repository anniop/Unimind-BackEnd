from __future__ import print_function
import sys
from logging.config import fileConfig
from sqlalchemy import create_engine
from sqlalchemy import pool
from sqlalchemy.ext.declarative import declarative_base
from alembic import context

from app.database import Base  # Import your Base class from app/database.py

# this is the Alembic Config object, which provides access to
# the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
fileConfig(config.config_file_name)

# Add your model's MetaData object here
target_metadata = Base.metadata  # Use your application's metadata
# target_metadata = None  # If no metadata object

def run_migrations_online():
    # This function is used for running migrations in an "online" mode
    # i.e. the database connection is established within this function
    connectable = create_engine(config.get_main_option("sqlalchemy.url"))
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True  # This ensures that column type differences are detected
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    print("Running in offline mode...")
else:
    run_migrations_online()
