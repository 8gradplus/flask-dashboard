from app import create_app

if __name__ == '__main__':
    app = create_app()
    # todo get configs from port
    app.run(debug=True, host='0.0.0.0', port=5000)

