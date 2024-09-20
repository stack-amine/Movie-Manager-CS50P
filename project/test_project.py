import pytest
import emoji
from project import add_movie, load_movies, search_movies, remove_movie, view_top_rated

def test_add_movie():
    result = add_movie("Inception", "Sci-Fi", 4.6)
    assert result == emoji.emojize("\n'Inception' added successfully:partying_face:")

def test_load_movies():
    result = load_movies()
    assert "Inception" in result

def test_view_top_rated():
    result = view_top_rated()
    assert "Inception" in result

def test_search_movies():
    result = search_movies("title", "Inception")
    assert "Inception" in result

def test_remove_movie():
    result = remove_movie("Inception")
    assert result == "\nInception has been removed!\n"
