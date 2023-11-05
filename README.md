# Flask Blog App

This Flask Blog App is a lightweight and user-friendly web application designed for creating, managing, and sharing blog posts. With this app, you can easily publish your thoughts, stories, and articles in a clean and organized manner.

## Features

- **User Authentication**: Users can create accounts, log in, and log out securely. Passwords are hashed for enhanced security.
- **Blog Post Management**: Authenticated users can create, edit, and delete their blog posts. Each post can include a title, content, and optional images.
- **Comment System**: Users can leave comments on blog posts. Comments are displayed below each post and can be moderated by the post author.
- **Responsive Design**: The app is responsive and can be accessed from various devices, including desktops, tablets, and smartphones.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/flask-blog-app.git
   cd flask-blog-app
   ```

2. **Create a Virtual Environment** (Optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**:

   - Create a database (SQLite, MySQL, PostgreSQL, etc.).
   - Update the `config.py` file with your database connection URI.

5. **Initialize the Database**:

   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

6. **Run the Application**:

   ```bash
   flask run
   ```

7. **Access the App**:

   Visit `http://localhost:5000` in your web browser to access the Flask Blog App.

## Configuration

- Update the `config.py` file to customize app settings, such as secret key, database URI, and other configuration options.

## Usage

- **Create an Account**: Start by creating a new account or log in if you already have one.
- **Create a Blog Post**: After logging in, click on "New Post" to create a new blog post. Provide a title, content, and optional images.
- **Manage Posts**: Authenticated users can edit or delete their existing posts from the dashboard.
- **Leave Comments**: Users can leave comments on blog posts. Comments are displayed below each post and can be moderated by the post author.

## Contributing

If you wish to contribute to the development of this Flask Blog App, please follow the guidelines outlined in the `CONTRIBUTING.md` file.
