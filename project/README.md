# Movie Manager

## Description

The **Movie Manager** is a command-line application designed to help users manage their personal movie collections efficiently. This program allows users to load all movies as needed. The application is built using Python and utilizes CSV file for data storage, providing a simple and effective way to maintain the movie database.

The Movie Manager is ideal for film enthusiasts who want to keep track of their watched films, explore new genres, and manage ratings. the user interface is straightforward and interactive, guiding users through the various functionalities with clear prompts and messages.

### Project Structure

The project consists of a single Python file, `project.py`, which contains all the necessary functions to run the application, also a `test_project.py` to test functions used in the project. Below is a brief description of the main components and their responsibilities:

-**Main Functionality**:
    -**`main()`**: the heart of the application, this function presents a menu to the user , processes their input, and calls the appropriate functions based on the user's choice. It ensures a seamless user experience by looping until the user decides to exit.
    -**`load_movies()`**: This function reads the movie data from the `movie.csv` file and formats it for display. It includes error handling to manage cases where the file does not exist or contains invalid data.
    -**`add_movie()`**: Responsible for adding a new movie entry to teh CSV file. It checks for teh existence of the file and creates a new header row if the file is empty.
    -**`remove_movie()`**: this function removes a movie from the collection based on its title. It handles the logic of reading the current list of movies, filtering out the one to be removed, and writing the updated list back to the CSV file.

-**Viewing and Searching**:
    -**`view_top_rated()`**: Displays the top five movies based on user ratings. It sorts the movies in descending order and uses star emojis to represent ratings visiually.
    -**`seach_movies()`**: Implements fuzzy matching to search for movies by title or genre. This functionality allows for flexibility in user input, making it easier to find matches even if the search terms are not exact

-**Utitlity Functions**:
    -**`convert_rating_to_stars()`**: A helper function that converts numerical ratings into a visually appealing string of star emojis, enhacing the user interface.

### Design Choices

Several design choices were made throughout the development of this application to enhance usability:

1. **Data Storage**: The decision to use a CSV file for storage was driven by its simplicity and ease of manipulation. This format allows for straightforward reading and writing without requiring complex database management.

2. **Error handling**: Robust error handling is implemented to manage potential issues, such as missing files and invalid user inputs. This design choice improves user experience by providing clear feedback when errors occur.

3. **User Interface**: The command-line interface was designed to be intuitive. By prompting users for input within the main function, the application maintains a conversational flow that is easy to follow.

4. **Fuzzy Matching**: the use of the `fuzywuzzy` library for search functionality was chosen to provide a more forgiving user experience. This allows users to find movies even if they are unsure of the exact title or genre.

In conclusion, the Movie Manager is a comprehensive tool for managing a movie collection with a user-friendly interface and effective data handling.
