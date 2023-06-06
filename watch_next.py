import spacy

def find_similar_movie(description):
    nlp = spacy.load('en_core_web_md')

    # Load the movies.txt file and extract movie descriptions
    with open('movies.txt', 'r') as file:
        movie_descriptions = file.read().splitlines()

    # Calculate similarity scores between the given description and all movie descriptions
    similarity_scores = []
    for movie_description in movie_descriptions:
        similarity_scores.append(nlp(description).similarity(nlp(movie_description)))

    # Find the index of the most similar movie
    most_similar_index = max(range(len(similarity_scores)), key=similarity_scores.__getitem__)

    # Print the index of the most similar movie
    print("Index of the most similar movie:", most_similar_index)

# Example usage
description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
find_similar_movie(description)
