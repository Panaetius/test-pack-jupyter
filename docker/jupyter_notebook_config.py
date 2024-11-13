import os

c.NotebookApp.ip = "0.0.0.0"
c.NotebookApp.port = 8888
c.NotebookApp.token = os.environ["SERVER_APP_TOKEN"]
c.NotebookApp.allow_origin = "https://renkulab.io"
c.NotebookApp.allow_remote_access = True
c.ContentsManager.allow_hidden = True
