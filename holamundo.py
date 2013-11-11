import web

urls = (
  '/', 'index'
)

app = web.application(urls, globals())

class index:
  def GET(self):
    return "Hola, Mundo"

if __name__ == "__main__":
  app.run()
