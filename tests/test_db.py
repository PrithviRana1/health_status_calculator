from testcontainers.postgres import PostgresContainer
import unittest
import datetime
from unittest.mock import patch
import psycopg2
from core import calculation


class TestDB(unittest.TestCase):

    def start_postgres_container(self):
        postgres_container = PostgresContainer("postgres:latest")
        postgres_container.start()
        return postgres_container

    def create_test_database(self, container):
        connection = psycopg2.connect(
            host=container.get_container_host_ip(),
            port=container.get_exposed_port(5432),
            user="test",
            password="test",
            cursor_factory=psycopg2.extras.DictCursor,
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute("CREATE DATABASE testdb")
        connection.close()

    @patch.object(calculation.Calc, 'all_statuses')
    def test_postgres_container(self, mock):
        obj = calculation.Calc()
        mock.return_value = [(0, {'owner': 'testO', 'repo': 'testR',
                                  'base': 'testB', 'head':
                                  'testH', 'apiV': '2022-11-28',
                                  'accept': 'application/vnd.github+json',
                                  'token': 'test',
                                  'datetime': datetime.datetime(2023, 4,
                                                                4, 15, 24,
                                                                17, 544269)})]

        with self.start_postgres_container() as postgres_container:
            self.create_test_database(postgres_container)
            connection = psycopg2.connect(
                host=postgres_container.get_container_host_ip(),
                port=postgres_container.get_exposed_port(5432),
                user="test",
                password="test",
                database="testdb",
                cursor_factory=psycopg2.extras.DictCursor,
            )
            with connection.cursor() as cursor:
                statuses = obj.all_statuses()
                cursor.execute("CREATE TABLE test_table"
                               "(repo_owner VARCHAR (50) NOT NULL,"
                               "repo VARCHAR (50) NOT NULL,"
                               "base VARCHAR (50) NOT NULL,"
                               "head VARCHAR(50) NOT NULL,"
                               "health_status DECIMAL,"
                               "date_time TIMESTAMP NOT NULL)")
                for status in statuses:
                    values = (status[1]['owner'], status[1]['repo'],
                              status[1]['base'],
                              status[1]['head'],
                              status[0], status[1]['datetime'])
                    insert_statement = """
                        INSERT INTO test_table (repo_owner,
                         repo, base, head, health_status, date_time)
                         VALUES (%s, %s, %s, %s, %s, %s)
                                        """
                    cursor.execute(insert_statement, values)
                connection.commit()
                cursor.execute("SELECT * FROM test_table")
                result = cursor.fetchall()
                assert result == [['testO', 'testR', 'testB',
                                  'testH', 0, datetime.datetime(2023, 4, 4,
                                                                15, 24, 17,
                                                                544269)]]
            connection.close()
