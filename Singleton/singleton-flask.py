# -*- coding: utf-8 -*-

import sqlite3
from flask import current_app
from flask import _app_ctx_stack as stack


class SQLite3(object):
    
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        
        app.config.setdefault('SQLITE3_DATABASE', ':memory:')
        app.teardown_appcontext(self.teardown)

    def connect(self):
        # connect to sqlite database
        return sqlite3.connect(current_app.config['SQLITE3_DATABASE'])
    
    def teardown(self, exception):
        # close sqlite connection
        ctx = stack.top
        if hasattr(ctx, 'sqlite3_db'):
            ctx.sqlite3_db.close()

    @property
    def connection(self):
        # use flask._app_ctx_stack to store sqlite connection
        # connection is used to connect to the database every time when connection is needed
        ctx = stack.top
        if ctx is not None:
            if not hasattr(ctx,'sqlite3_db'):
                ctx.sqlite3_db = self.connect()
            return ctx.sqlite3_db
