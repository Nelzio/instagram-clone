# Instagram Clone

This is a Django-based project that replicates some of the core functionalities of Instagram.

## Features

- User authentication (signup, login, logout)
- Profile creation and editing
- Photo upload and display
- Like and comment on photos
- Follow and unfollow users

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Nelzio/instagram-clone.git
    cd instagram-clone
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

- Access the application at `http://127.0.0.1:8000/`
- Register a new account or log in with an existing one
- Start uploading photos, following users, and interacting with posts

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, please contact [your-email@example.com](mailto:your-email@example.com).
