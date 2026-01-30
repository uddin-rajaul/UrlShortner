# Django URL Shortener

A modern, full-featured URL shortener built with Django 5 and Tailwind CSS. Create, manage, and track shortened links with a beautiful, responsive interface.

## Features

- **URL Shortening**: Convert long URLs into compact, shareable links.
- **Custom Aliases**: Create meaningful custom short codes (e.g., `yoursite.com/my-link`).
- **Analytics**: Track click counts for each of your links.
- **QR Codes**: Automatically generate QR codes for every shortened URL.
- **User Authentication**: Secure signup and login system to manage your personal links.
- **Responsive Design**: Built with Tailwind CSS for a seamless experience on mobile and desktop.
- **Fast & Secure**: Built on the robust Django framework.

## Tech Stack

- **Backend**: Python, Django 5.x
- **Database**: SQLite (Default), extensible to PostgreSQL/MySQL
- **Frontend**: HTML5, Tailwind CSS
- **Utilities**: QRious (JS library for QR generation)

## Installation

Follow these steps to set up the project locally:

1.  **Clone the repository**
    ```bash
    git clone https://github.com/yourusername/url-shortner.git
    cd url-shortner
    ```

2.  **Create and activate a virtual environment**
    ```bash
    # Linux/macOS
    python3 -m venv .venv
    source .venv/bin/activate

    # Windows
    # python -m venv .venv
    # .venv\Scripts\activate
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations**
    ```bash
    python manage.py migrate
    ```

5.  **Run the development server**
    ```bash
    python manage.py runserver
    ```

6.  Open your browser and navigate to `http://127.0.0.1:8000/`.

## Usage

1.  **Register** for a new account or **Log in**.
2.  Click **"Create Short URL"** on the dashboard.
3.  Paste your long URL. Optionally, provide a custom short code.
4.  Copy your new short link or download the generated QR code!
5.  View your dashboard to see how many times your link has been visited.
