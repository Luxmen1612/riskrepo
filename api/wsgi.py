from api.app import init_app
import sys

app = init_app()
app.config['SECRET_KEY'] = 'any secret string'

if __name__ == "__main__":

    port = sys.argv[1]
    app.run(host = '0.0.0.0', port = port)