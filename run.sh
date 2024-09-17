# Find the PID of the Django server process
SERVER_PID=$(ps aux | grep '[m]anage.py runserver' | awk '{print $2}')

# Check if we found the PID
if [ -n "$SERVER_PID" ]; then
    # Kill the server process
    kill $SERVER_PID
    echo "Server stopped."
else
    # Save the current directory
    ORIGINAL_DIR=$(pwd)

    # Navigate to your Django project directory
    cd ~/pierrelaurs-todo-app

    # Activate your virtual environment if needed
    # source venv/bin/activate

    # Start the Django development server
    python manage.py runserver &

    # Open the default web browser with the application
    cmd.exe /c start http://127.0.0.1:8000

    # Return to the original directory
    cd "$ORIGINAL_DIR"
    echo "Server started."
fi
