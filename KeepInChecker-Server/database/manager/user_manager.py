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


import sys
sys.path.append('../..')

from constants import database_path, database_user, database_password
from ..db_session import DbSession


class UserManager(object):

    def __init__(self):
        self.database_path = database_path
        self.user = database_user
        self.password = database_password

        self.db = DbSession(database_path, database_user, database_password)
