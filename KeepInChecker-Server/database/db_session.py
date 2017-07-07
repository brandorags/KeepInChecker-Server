# Copyright 2017 Brandon Ragsdale
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import sqlite3


class DbSession(object):
    """
    This class provides a layer of abstraction for
    when performing database transactions.
    """

    def __init__(self, path):
        """
        Constructor for DbSession.

        :param path: the path to the database
        """
        self.database_path = path

        self.connection = sqlite3.connect(self.database_path)
        self.connection.text_factory = str
        self.connection.row_factory = sqlite3.Row

        self.cursor = self.connection.cursor()

    def execute(self, sql):
        """
        Executes the given SQL query.

        :param sql: the SQL query
        """
        self.cursor.execute(sql)

    def commit(self):
        """
        Commits the database transaction. close(self) must be called after
        this method to successfully disconnect from the database.
        """
        self.connection.commit()

    def close(self):
        """
        Terminates the connection to the database.
        """
        self.cursor.close()
        self.connection.close()

    def commit_and_close(self):
        """
        Commits and closes the transaction.
        """
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
