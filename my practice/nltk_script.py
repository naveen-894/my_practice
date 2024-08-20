import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Example job skills and candidate skills
job_skills = ['frontend development', 'javascript', 'node js']
candidate_skills = ['backend development', 'html', 'css', 'postgres']

# Tokenization and preprocessing
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    tokens = word_tokenize(text.lower())  # Tokenize and lowercase
    tokens = [token for token in tokens if token.isalnum() and token not in stop_words]  # Remove stopwords and punctuation
    return tokens

# Calculate similarity based on WordNet semantic similarity
def calculate_similarity(skill1, skill2):
    skill1_words = preprocess_text(skill1)
    skill2_words = preprocess_text(skill2)
    
    max_similarity = 0.0
    for word1 in skill1_words:
        synsets1 = wordnet.synsets(word1)
        for word2 in skill2_words:
            synsets2 = wordnet.synsets(word2)
            if synsets1 and synsets2:
                for synset1 in synsets1:
                    for synset2 in synsets2:
                        similarity = synset1.path_similarity(synset2) or 0
                        if similarity > max_similarity:
                            max_similarity = similarity
    return max_similarity

# Calculate overall similarity score
def calculate_matching_matrix(job_skills, candidate_skills):
    matching_matrix = []
    
    for candidate_skill in candidate_skills:
        row = []
        for job_skill in job_skills:
            similarity = calculate_similarity(candidate_skill, job_skill)
            row.append(similarity)
        matching_matrix.append(row)
    
    return matching_matrix

# Calculate matching matrix
matching_matrix = calculate_matching_matrix(job_skills, candidate_skills)

# Print results in matrix format
header = f"{'':<25}" + "".join([f"{job_skill:<20}" for job_skill in job_skills])
print(header)
for i, candidate_skill in enumerate(candidate_skills):
    row = f"{candidate_skill:<25}" + "".join([f"{score:<20.2f}" for score in matching_matrix[i]])
    print(row)

# Calculate overall matching percentage
total_score = sum(max(row) for row in matching_matrix)
matching_percentage = (total_score / len(job_skills)) * 100

print(f"\nOverall Matching Percentage: {matching_percentage:.2f}%")