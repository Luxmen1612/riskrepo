from api.app import init_app

app = init_app()
app.config['SECRET_KEY'] = 'any secret string'

if __name__ == "__main__":
    app.run(host = '0.0.0.0')