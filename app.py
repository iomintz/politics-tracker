#!/usr/bin/env python3

# SPDX-License-Identifier: GPL-2.0-or-later
# See LICENSE.md for details

from quart import Quart

app = Quart(__name__)

@app.route('/')
async def hello():
    return 'hello'

if __name__ == '__main__':
	app.run()
