from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Combine skills for TF-IDF vectorization
# job_skills = ['frontend development', 'javascript', 'node js']
# candidate_skills = ['backend development', 'frontend', 'python', 'postgres']
job_skills = ['problem-solving', 'automation', 'network security', 'cloud computing']
candidate_skills = ['troubleshooting', 'scripting', 'encryption', 'AWS']
# candidate_skills = ['sales manager', 'sales', 'marketing management',]
all_skills = job_skills + candidate_skills

# Vectorize using TF-IDF
vectorizer = TfidfVectorizer().fit_transform(all_skills)
vectors = vectorizer.toarray()

# Split vectors into job and candidate vectors
job_vectors = vectors[:len(job_skills)]
candidate_vectors = vectors[len(job_skills):]

# Calculate cosine similarity
similarity_matrix = cosine_similarity(candidate_vectors, job_vectors)

# Display similarity scores
df_tfidf = pd.DataFrame(similarity_matrix, columns=job_skills, index=candidate_skills)
print("TF-IDF and Cosine Similarity:")
print(df_tfidf)