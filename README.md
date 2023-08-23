# Honolulu Climate Analysis Project

Congratulations on embarking on your climate analysis project in Honolulu, Hawaii! This README provides an overview of my project and guides users on how to use my code and Flask API.

## Project Overview

I've decided to treat myself to a long holiday vacation in Honolulu, Hawaii, and to help with my trip planning, I've performed a climate analysis of the area. This project consists of two main parts:

- Part 1: Analyze and Explore the Climate Data
  - Perform a precipitation analysis and a station analysis using Python, SQLAlchemy, and Pandas.
  - Visualize the data with Matplotlib.
- Part 2: Design Your Climate App
  - Create a Flask API with various routes to access the analysis results.

## Part 1: Analyze and Explore the Climate Data

### Prerequisites

Before running the code, make sure you have the following:

- Python
- Jupyter Notebook
- SQLAlchemy
- Pandas
- Matplotlib
- SQLite database (hawaii.sqlite) and the provided Jupyter Notebook (climate_starter.ipynb).

### Instructions

1. Use SQLAlchemy to connect to the SQLite database.
2. Reflect the tables into classes using SQLAlchemy's automap_base function.
3. Perform a precipitation analysis by finding the most recent date and querying the previous 12 months of precipitation data.
4. Perform a station analysis to calculate the total number of stations and find the most-active station.
5. Query temperature observation (TOBS) data for the most-active station for the previous year.
6. Close the SQLAlchemy session.

## Part 2: Design Your Climate App

### Flask API Routes

- `/`: Homepage
- `/api/v1.0/precipitation`: Retrieve the last 12 months of precipitation data.
- `/api/v1.0/stations`: List all available weather stations.
- `/api/v1.0/tobs`: Retrieve temperature observations for the most-active station in the last year.
- `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`: Get temperature statistics for a specified start date or date range.

### How to Run the Flask App

1. Make sure you have Flask installed (`pip install Flask`).
2. Run the Flask app by executing `app.py`.

## Example Usage

Here's an example of how to use the API routes:

- To get precipitation data: `/api/v1.0/precipitation`
- To get station information: `/api/v1.0/stations`
- To get temperature observations: `/api/v1.0/tobs`
- To get temperature statistics for a specific date range: `/api/v1.0/<start>` or `/api/v1.0/<start>/<end>`

## Closing Notes

Feel free to explore and extend this project further. Contributions and feedback are always welcome.

Happy climate analysis and enjoy your vacation in Honolulu!

