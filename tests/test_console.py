#!/usr/bin/python3
"""Unit test module for the console (command interpreter).
"""
import json
import unittest
from io import StringIO
from unittest.mock import patch
import MySQLdb
import os
import sqlalchemy

from models.base_model import BaseModel
from models.user import User
from tests import clear_stream
from console import HBNBCommand
from models import storage



class TestHBNBCommand(unittest.TestCase):
    """This is the class for the HBNBCommand
    """
    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_fs_create(self):
        """USe file storage to test the create command.
        """
        with patch('sys.stdout', new=StringIO()) as cout:
            my_console = HBNBCommand()
            my_console.onecmd('create City name="Texas"')
            mdl_id = cout.getvalue().strip()
            clear_stream(cout)
            self.assertIn('City.{}'.format(mdl_id), storage.all().keys())
            my_console.onecmd('show City {}'.format(mdl_id))
            self.assertIn("'name': 'Texas'", cout.getvalue().strip())
            clear_stream(cout)
            my_console.onecmd('create User name="Kevin" age=17 height=5.9')
            mdl_id = cout.getvalue().strip()
            self.assertIn('User.{}'.format(mdl_id), storage.all().keys())
            clear_stream(cout)
            my_console.onecmd('show User {}'.format(mdl_id))
            self.assertIn("'name': 'Kevin'", cout.getvalue().strip())
            self.assertIn("'age': 17", cout.getvalue().strip())
            self.assertIn("'height': 5.9", cout.getvalue().strip())

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') != 'db', 'DBStorage test')
    def test_db_create(self):
        """Use Database storage to test teh create command.
        """
        with patch('sys.stdout', new=StringIO()) as cout:
            my_console = HBNBCommand()
            # creating a model with non-null attribute(s)
            with self.assertRaises(sqlalchemy.exc.OperationalError):
                my_console.onecmd('create User')
            # creating a User instance
            clear_stream(cout)
            my_console.onecmd('create User email="kane02@gmail.com" password="454"')
            mdl_id = cout.getvalue().strip()
            conn = MySQLdb.connect(
                host=os.getenv('HBNB_MYSQL_HOST'),
                port=3306,
                user=os.getenv('HBNB_MYSQL_USER'),
                passwd=os.getenv('HBNB_MYSQL_PWD'),
                db=os.getenv('HBNB_MYSQL_DB')
            )
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE id="{}"'.format(mdl_id))
            response = cursor.fetchone()
            self.assertTrue(response is not None)
            self.assertIn('kane02@gmail.com', response)
            self.assertIn('454', response)
            cursor.close()
            conn.close()

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') != 'db', 'DBStorage test')
    def test_db_count(self):
        """Use database storage to test count command.
        """
        with patch('sys.stdout', new=StringIO()) as cout:
            my_console = HBNBCommand()
            conn = MySQLdb.connect(
                host=os.getenv('HBNB_MYSQL_HOST'),
                port=3306,
                user=os.getenv('HBNB_MYSQL_USER'),
                passwd=os.getenv('HBNB_MYSQL_PWD'),
                db=os.getenv('HBNB_MYSQL_DB')
            )
            cursor = conn.cursor()
            cursor.execute('SELECT COUNT(*) FROM states;')
            res = cursor.fetchone()
            prev_value = int(res[0])
            my_console.onecmd('create State name="Enugu"')
            clear_stream(cout)
            my_console.onecmd('count State')
            cnt = cout.getvalue().strip()
            self.assertEqual(int(cnt), prev_value + 1)
            clear_stream(cout)
            my_console.onecmd('count State')
            cursor.close()
            conn.close()


    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') != 'db', 'DBStorage test')
    def test_db_show(self):
        """Use database storage to test show command.
        """
        with patch('sys.stdout', new=StringIO()) as cout:
            my_console = HBNBCommand()
            # showing a User instance
            object = User(email="kane02@gmail.com", password="454")
            conn = MySQLdb.connect(
                host=os.getenv('HBNB_MYSQL_HOST'),
                port=3306,
                user=os.getenv('HBNB_MYSQL_USER'),
                passwd=os.getenv('HBNB_MYSQL_PWD'),
                db=os.getenv('HBNB_MYSQL_DB')
            )
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE id="{}"'.format(object.id))
            response = cursor.fetchone()
            self.assertTrue(response is None)
            my_console.onecmd('show User {}'.format(object.id))
            self.assertEqual(
                cout.getvalue().strip(),
                '** no instance found **'
            )
            object.save()
            conn = MySQLdb.connect(
                host=os.getenv('HBNB_MYSQL_HOST'),
                port=3306,
                user=os.getenv('HBNB_MYSQL_USER'),
                passwd=os.getenv('HBNB_MYSQL_PWD'),
                db=os.getenv('HBNB_MYSQL_DB')
            )
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE id="{}"'.format(object.id))
            clear_stream(cout)
            my_console.onecmd('show User {}'.format(object.id))
            response = cursor.fetchone()
            self.assertTrue(response is not None)
            self.assertIn('kane02@gmail.com', response)
            self.assertIn('454', response)
            self.assertIn('kane02@gmail.com', cout.getvalue())
            self.assertIn('454', cout.getvalue())
            cursor.close()
            conn.close()


