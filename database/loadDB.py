from database import connection


class DB:
    def __init__(self):
        self.conn_obj = connection.Connect()

    def load(self, status):
        conn = self.conn_obj.conn

        # Define the values to be inserted
        values = (status[1]['owner'], status[1]['repo'], status[1]['base'],
                  status[1]['head'], status[0], status[1]['datetime'])

        try:
            with conn:
                with conn.cursor() as cur:
                    insert_statement = """
                        INSERT INTO healthStatus (repo_owner,
                         repo, base, head, health_status, date_time)
                         VALUES (%s, %s, %s, %s, %s, %s)
                                        """
                    cur.execute(insert_statement, values)

        except Exception as e:
            print(f"Error: {e}")
            conn.rollback()
        else:
            conn.commit()
