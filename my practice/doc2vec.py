from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import pandas as pd
import numpy_practice as np

# Define job and candidate skills
job_skills = ['frontend development', 'javascript', 'node js']
candidate_skills = ['backend development', 'java', 'python', 'postgres']
all_skills = job_skills + candidate_skills

# Tag each skill with a unique identifier
tagged_data = [TaggedDocument(words=skill.split(), tags=[str(i)]) for i, skill in enumerate(all_skills)]

# Initialize and train the Doc2Vec model
model = Doc2Vec(vector_size=20, min_count=1, epochs=20)
model.build_vocab(tagged_data)
model.train(tagged_data, total_examples=model.corpus_count, epochs=model.epochs)

# Infer vectors for job skills and candidate skills
job_vectors = [model.infer_vector(skill.split()) for skill in job_skills]
candidate_vectors = [model.infer_vector(skill.split()) for skill in candidate_skills]

# Compute cosine similarity manually
def cosine_similarity(v1, v2):
    dot_product = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    return dot_product / (norm_v1 * norm_v2)

similarity_matrix = [
    [cosine_similarity(candidate_vec, job_vec) for job_vec in job_vectors]
    for candidate_vec in candidate_vectors
]

# Convert to DataFrame for better readability
df_doc2vec = pd.DataFrame(similarity_matrix, index=candidate_skills, columns=job_skills)
print(df_doc2vec)
