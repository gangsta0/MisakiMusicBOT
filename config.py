# Calls Music 1 - Telegram bot for streaming audio in group calls
# Copyright (C) 2021  Roj Serbest

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# Modified by Inukaasith 

from os import getenv

from dotenv import load_dotenv

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "AgB3xbXniS5D9poBCj45l2GAQaeeUmLoZY5H-RlRdDQzt4rMfQdpwF8T0arA5nmd22aLL00DAHYIn3wtbZrcSHnU9IbZzA5mvoLZvcHck4KvR1IYF8wefegxc2G8P1iJvWBtCbzO4o0pYhb4mG5yq1ZdXTKr-3fzrt3N9tHyYTTgCW6G1DG1FQyxgsw9BbEM7YDqC-8xeOq_gsV4ucIURHNoM8X1rzD0AQWdIj9OkTAv-8R163UWrDzsshsESjWKevDHZ9gA92WnGZqXh96B93_2PH_FyjM72PjUF-B9QR2zdWejnMrFBlO7bA7BhXDlSfvmv-5kDik39ULxkD2dacGAAAAAAUdE-iwA")
BOT_TOKEN = getenv("5658502641:AAFg_0wViDGxf1h2JolViCOSfHfZk2Sd0K0")
BOT_NAME = getenv("Nurlandi")
admins = {}
API_ID = int("1225523")
API_HASH = getenv("ec0ae6e668e4eaa669c536acf13c9f59")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = int("1339412165")
