from app import app

if __name__ == '__main__':
    with app.app_context():
     # Ensure database tables are created
        app.run(debug=True)