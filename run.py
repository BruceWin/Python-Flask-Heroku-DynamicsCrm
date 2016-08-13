import sys

port = int(sys.argv[2])

from app import app
app.run(debug=True,host='0.0.0.0', port=port)
