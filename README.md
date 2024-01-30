YouTube to MP4 Converter

This is a simple Flask web application that allows users to convert YouTube videos to MP4 format and download them. The application utilizes the pytube library for handling YouTube video downloads.
Requirements

Make sure you have the required Python packages installed using the following:
pip install pytube Flask
python app.py

    Open your web browser and navigate to the http:// adress given in the terminal to access the converter.

    Enter the YouTube video URL in the provided input field.

    Click the "Convert to MP4" button.

    The converted video will be available for download with a clean title.

Code Explanation
Server-side (your_script_name.py)

    import statements: Imports necessary modules and libraries, including Flask for the web application and pytube for handling YouTube video downloads.

    @app.route("/"): Defines the route for the index page, rendering the index.html template.

    @app.route("/favicon.ico"): Defines the route for serving the favicon.

    @app.route("/hello", methods=["POST"]): Defines the route for handling form submissions. Extracts the YouTube video URL from the submitted form, downloads the video, and serves it as a response.

    if __name__ == "__main__":: Starts the Flask application.

Client-side (templates/index.html)

    HTML template for the web application with a form allowing users to input a YouTube video URL and convert it to MP4.

    Basic styling with CSS to enhance the visual appearance of the form.

Note

    Ensure that you have a stable internet connection while using the application to download YouTube videos.

    This application is intended for personal use, and the downloading of YouTube videos may be subject to YouTube's terms of service.

    The code uses the Flask development server, which is not suitable for production. Consider deploying the application with a production-ready server for a production environment.

    The application currently supports video downloads in the highest resolution available. You may customize the code to include additional features or modify the resolution selection logic as needed.