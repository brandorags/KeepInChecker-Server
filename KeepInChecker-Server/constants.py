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


from configparser import ConfigParser


# global server config objects
database_path = ''
database_user = ''
database_password = ''


def initialize_constants():
    global database_path
    global database_user
    global database_password

    config = ConfigParser()
    config.read('../server.cfg')

    database_path = config['database']['DATABASE_PATH']
    database_user = config['database']['DATABASE_USER']
    database_password = config['database']['DATABASE_PASSWORD']
