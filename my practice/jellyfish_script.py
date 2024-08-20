import jellyfish
import pandas as pd

# Define job and candidate skills
# job_skills = ['data analysis', 'SQL', 'tableau', 'machine learning']
# candidate_skills = ['python', 'excel', 'data visualization', 'R']

# job_skills = ['recruitment', 'employee relations', 'training and development', 'HRIS']
# candidate_skills = ['communication skills', 'Microsoft Excel', 'project management', 'talent acquisition', 'recruitment']

job_skills = ['problem-solving', 'automation', 'network security', 'cloud computing']
candidate_skills = ['troubleshooting', 'scripting', 'encryption', 'AWS']

# Calculate Jaro-Winkler similarity
def jaro_winkler_similarity(skills1, skills2):
    similarity = []
    for s1 in skills1:
        row = []
        for s2 in skills2:
            score = jellyfish.jaro_winkler_similarity(s1, s2)
            row.append(score)
        similarity.append(row)
    return similarity

jaro_winkler_sim_matrix = jaro_winkler_similarity(candidate_skills, job_skills)

# Display similarity scores for Jaro-Winkler
df_jaro_winkler = pd.DataFrame(jaro_winkler_sim_matrix, columns=job_skills, index=candidate_skills)

print("Jelly-fish Similarity:")
print(df_jaro_winkler)
