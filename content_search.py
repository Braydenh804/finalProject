from tkinter import *



def search_movie_file(entry):
    def read_tsv_file(filename):
        data_dict = {}
        with open(filename, 'r') as file:
            for line in file:
                columns = line.strip().split('\t')
                if len(columns) >= 3:
                    value_to_compare = columns[2].lower()  # Convert to lowercase for case-insensitive comparison
                    if value_to_compare not in data_dict:
                        data_dict[value_to_compare] = []
                    data_dict[value_to_compare].append(line.strip())  # Save the whole row

        return data_dict

    # Replace 'your_file.tsv' with the path to your TSV file
    searched_movie_data = read_tsv_file('ratedMovies.tsv')

    # For example, to access the rows where the third column matches a specific value (ignoring case)
    search_value = entry
    search_key = search_value.lower()

    if search_key in searched_movie_data:
        matching_rows = searched_movie_data[search_key]
        for row in matching_rows:
            print(row)  # Modify as needed, here printing the matching rows
    else:
        print("No matching rows found for", search_value)

