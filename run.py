#!/usr/bin/env python3
from app import app
context = ('cert.pem', 'privkey.pem')
app.run(debug=True, host="0.0.0.0", threaded=True, ssl_context=context)
