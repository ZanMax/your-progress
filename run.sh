#!/bin/bash

# Function to find a directory with settings.py file in the current directory
find_settings_directory() {
  for dir in */; do
    if [ -f "$dir/settings.py" ]; then
      SETTINGS_DIR="${dir%/}" # Remove trailing slash
      break
    fi
  done
}

# Function to start Uvicorn with the found settings directory
start_uvicorn() {
  find_settings_directory
  if [ -n "$SETTINGS_DIR" ]; then
    ASGI_MODULE="${SETTINGS_DIR}.asgi" # Use the correct module path
    echo "Starting Uvicorn for directory: $SETTINGS_DIR"
    uvicorn "$ASGI_MODULE:application" --reload
  else
    echo "No directory with settings.py found in the current directory."
  fi
}

# Display the menu to the user
show_menu() {
  echo "Choose an option:"
  echo "1) Dev server"
  echo "2) Uvicorn"
  echo "3) Migrate"
  echo "4) Collect Static"
  echo "5) Docker Compose Up"
  echo "6) Docker Compose Down"
  echo "7) Pip Upgrade"
  echo "8) Exit"
}

# Infinite loop to display the menu until the user chooses to exit
while true; do
  show_menu

  read -p "Enter your choice (1-8): " choice

  case $choice in
  1)
    echo "Starting dev server..."
    python3 manage.py runserver
    ;;

  2)
    start_uvicorn
    ;;

  3)
    echo "Running makemigrations..."
    python3 manage.py makemigrations

    echo "Running migrate..."
    python3 manage.py migrate

    echo "Migration completed successfully!"
    ;;

  4)
    echo "Removing old staticfiles..."
    rm -rf staticfiles

    echo "Collecting static files..."
    python3 manage.py collectstatic
    ;;

  5)
    echo "Running: docker-compose up -d --build"
    docker-compose up -d --build
    ;;

  6)
    echo "Running: docker-compose down --rmi all"
    docker-compose down --rmi all
    ;;

  7)
    echo "Running: pip install -r requirements.txt --upgrade"
    pip install -r requirements.txt --upgrade
    ;;

  8)
    echo "Exiting..."
    exit 0
    ;;

  *)
    echo "Invalid choice. Please choose between 1-8."
    ;;
  esac
done
