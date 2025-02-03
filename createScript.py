import csv
import json
import sys
from datetime import datetime
import os

def convert_csv_to_json(csv_file_path):
    # List to store movie data
    movies = []
    
    # Read CSV file
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # Extract only the required fields
            movie = {
                'title': row['Title'],
                'dateRated': row['Date Rated']
            }
            movies.append(movie)   
    return movies

def create_js_file(movie_data):
    # Get current timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Read template file
    template_path = 'imdbtemplate.js'
    with open(template_path, 'r', encoding='utf-8') as template_file:
        template_content = template_file.read()
    
    # Convert movie data to JSON string
    movie_json = json.dumps(movie_data, indent=2)
    
    # Replace placeholder in template with actual data
    new_content = template_content.replace('const movieData = [];', f'const movieData = {movie_json};')
    
    # Create new filename with timestamp
    output_filename = f'imdbDateInjector-{timestamp}.js'
    
    # Write to new file
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        output_file.write(new_content)
    
    return output_filename

def main():
    # Check if input file is specified
    if len(sys.argv) < 2:
        print("Error: No input file specified")
        print("Usage: python createScript.py <ratings.csv>")
        sys.exit(1)
        
    # Check if input file has correct extension
    if not sys.argv[1].endswith('.csv'):
        print("Error: Input file must be a CSV file")
        print("Usage: python createScript.py <ratings.csv>") 
        sys.exit(1)
        
    csv_file = sys.argv[1]
    
    try:
        # Convert CSV to JSON
        movie_data = convert_csv_to_json(csv_file)
        
        # Create JS file with timestamp
        output_file = create_js_file(movie_data)
        
        print(f"Successfully created: {output_file}")
        
    except FileNotFoundError:
        print("Error: Input file not found!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
