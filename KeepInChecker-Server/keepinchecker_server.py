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


import constants

from database.manager.user_manager import UserManager
from database.db_initializer import DbInitializer
from flask import Flask


# global Flask object
app = Flask(__name__)


def init_server_config_objects():
    """
    Initializes the constants that represent the
    values specified in server.cfg
    """
    constants.initialize_constants()


def init_database():
    """
    Initializes the connection to the database and
    also creates the database tables if they don't
    already exist.
    """
    db_initializer = DbInitializer(constants.database_path,
                                   constants.database_user,
                                   constants.database_password)
    db_initializer.create_tables_if_none_exist()


if __name__ == '__main__':
    init_server_config_objects()
    init_database()
    app.run(host='0.0.0.0')
