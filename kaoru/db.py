# -*- coding: utf-8 -*-

"""
kaoru.db
~~~~~~~~

sqlite3 database module

:copyright: (c) 2015 by Alejandro Ricoveri
:license: MIT, see LICENSE for more details.

"""

import sqlite3
import os
import time

from . import log

#################
# Database schema
#################
_db_schema = """
CREATE TABLE updates (
   id      INTEGER PRIMARY KEY NOT NULL,
   usr_id  INTEGER NOT NULL,
   message TEXT NOT NULL
)
"""
_db_file = None # database file used by sqlite3

def _create_schema(db):
    """Generate new sqlite schema on database file"""
    log.msg_debug("Creating new sqlite3 db at {}".format(db))
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        cursor.execute(_db_schema)

def init(*, db):
    """Initialise database interface

    :param db: database file to use
    """

    # check whether the database file actually exists
    if not os.path.isfile(db):
        log.msg_warn("Database not found!, creating a new one ...")
        # create schema
        _create_schema(db)

    global _db_file
    _db_file = db

def insert_update(update):
    """Insert Telegram update into database"""

    update_id = update.update_id
    user_id = update.message.from_user.id
    message = update.message.text
    log.msg_debug("sqlite: inserting update '{}'".format(update_id))
    query("INSERT INTO updates VALUES({}, {}, '{}')".format(
            update_id, user_id, message
        )
    )

def get_last_update_id():
    """Get latest update_id"""

    rows = query("SELECT * FROM updates ORDER BY id DESC LIMIT 1")
    if len(rows):
        return rows[0][0]
    return None

def query(sql):
    """Perform query on database"""

    log.msg_debug("sqlite: connecting to database")
    rows = None
    start_time = time.time()
    with sqlite3.connect(_db_file) as conn:
        cursor = conn.cursor()
        log.msg_debug("sqlite: {}".format(sql))
        cursor.execute(sql)
        dt = time.time() - start_time
        log.msg_debug("sqlite: done ({:.3f} ms)".format(dt*1000))
        rows = cursor.fetchall()
        if len(rows):
            log.msg_debug("sqlite: got {} row(s)".format(len(rows)))
        else:
            log.msg_debug("sqlite: got nothing from this query")
    return rows

