from flask.cli import FlaskGroup

from coolGeoApp import app
from pathlib import Path
from coolGeoApp.db import get_db

cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    db = get_db()

    with app.open_resource('schema.sql', 'r') as fh: 
        sql_content = fh.read()

        with db.cursor() as cursor: 
            cursor.execute(sql_content)


if __name__ == '__main__':
    cli()