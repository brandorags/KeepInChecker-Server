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


from .db_session import DbSession


class DbInitializer(object):
    """
    This class is used simply for the purpose of creating tables
    that may not already exist.
    """

    def __init__(self, database_path, user, password):
        self.database_path = database_path
        self.user = user
        self.password = password

    def create_tables_if_none_exist(self):
        """
        Creates the tables for the database if they don't already exist.
        """
        db = DbSession(self.database_path, self.user, self.password)
        db.execute('''CREATE TABLE IF NOT EXISTS "User" (
                                    `UserId` TEXT NOT NULL,
                                    `SecurityKey` TEXT NOT NULL,
                                    PRIMARY KEY(UserId)
                                )''')
        db.commit_and_close()
