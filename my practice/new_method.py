import numpy_practice as np

def vectorize_skills(skills_list, all_skills):
    # Create a vector of length equal to the number of unique skills
    vector = [1 if skill in skills_list else 0 for skill in all_skills]
    return vector

def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    magnitude_vec1 = np.linalg.norm(vec1)
    magnitude_vec2 = np.linalg.norm(vec2)
    if magnitude_vec1 == 0 or magnitude_vec2 == 0:
        return 0.0
    return dot_product / (magnitude_vec1 * magnitude_vec2)

# Example usage:
# job_skills = ["Python", "SQL", "Machine Learning"]
# candidate_skills = [["Python", "Java", "SQL"], ["Python", "SQL"], ["Java", "C++"]]
job_skills = ['frontend development', 'javascript', 'node js']
candidate_skills = [['backend development', 'html', 'css', 'postgres']]

all_skills = list(set(job_skills + [skill for sublist in candidate_skills for skill in sublist]))

job_vector = vectorize_skills(job_skills, all_skills)
candidate_vectors = [vectorize_skills(skills, all_skills) for skills in candidate_skills]

similarities = [cosine_similarity(job_vector, candidate_vector) for candidate_vector in candidate_vectors]

for idx, similarity in enumerate(similarities):
    print(f"Candidate {idx+1} Similarity: {similarity}")