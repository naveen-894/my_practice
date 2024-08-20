import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import pandas as pd

# Load the Universal Sentence Encoder
model = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

# Define job and candidate skills
job_skills = ['frontend development', 'javascript', 'node js']
# candidate_skills = ['backend development', 'java', 'python', 'postgres']
candidate_skills = ['sales manager', 'sales', 'marketing management',]

# Generate embeddings
job_embeddings = model(job_skills)
candidate_embeddings = model(candidate_skills)

# Calculate cosine similarity
similarity_matrix = np.inner(candidate_embeddings, job_embeddings)

# Display similarity scores
df_use = pd.DataFrame(similarity_matrix, columns=job_skills, index=candidate_skills)
print("\nUniversal Sentence Encoder (USE) Similarity:")
print(df_use)