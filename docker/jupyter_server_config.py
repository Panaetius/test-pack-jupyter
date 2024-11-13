import os

c.ServerApp.ip = "0.0.0.0"
c.ServerApp.port = 8888
c.ServerApp.token = os.environ["SERVER_APP_TOKEN"]
c.ServerApp.allow_origin = "https://renkulab.io"
c.ServerApp.allow_remote_access = True
c.ContentsManager.allow_hidden = True
