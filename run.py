import os

from app import create_app


app = create_app("development")

port = int(os.environ.get('PORT', 33507))
app.run(host='0.0.0.0', port=port)
