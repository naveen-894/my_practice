# !python -m sentence-transformers
from datetime import datetime
print(datetime.now())
from sentence_transformers import SentenceTransformer, util
import pandas as pd
print(datetime.now())
print('initialization started')
import torch
from sentence_transformers import SentenceTransformer

device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(device)
model = SentenceTransformer('paraphrase-MiniLM-L6-v2', device=device)
# Initialize SBERT model
# model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
print('initialization ended')
# List of available models
# Define job and candidate skills
# job_skills = ['frontend development', 'javascript', 'node js']
# candidate_skills = ['backend development', 'html', 'css', 'postgres']
# candidate_skills = ['sales manager', 'sales', 'marketing management',]
# candidate_skills = ['backend development', 'java', 'python', 'postgres']

# job_skills = ['data analysis', 'SQL', 'tableau', 'machine learning']
# candidate_skills = ['python', 'excel', 'data visualization', 'R']

# job_skills = ['recruitment', 'employee relations', 'training and development', 'HRIS']
# candidate_skills = ['communication skills', 'Microsoft Excel', 'project management', 'talent acquisition', 'recruitment']

job_skills = ['problem-solving', 'automation', 'network security', 'cloud computing']
# candidate_skills = ['troubleshooting', 'scripting', 'encryption', 'AWS']

candidate_skills = [
    "Python", "Java", "C++", "JavaScript", "SQL", "HTML", "CSS", "React", "Angular", "Vue.js",
    "Django", "Flask", "Spring Boot", "Node.js", "Express.js", "Ruby on Rails", "ASP.NET", "Laravel", "Kubernetes", "Docker",
    "AWS", "Azure", "Google Cloud", "Linux", "Windows Server", "Unix", "Bash", "PowerShell", "Git", "GitHub",
    "CI/CD", "Jenkins", "Travis CI", "CircleCI", "Ansible", "Puppet", "Chef", "Terraform", "Nagios", "Prometheus",
    "Grafana", "Splunk", "Elasticsearch", "Logstash", "Kibana", "Tableau", "Power BI", "QlikView", "SAP", "Oracle",
    "Salesforce", "Microsoft Dynamics", "HubSpot", "Marketo", "Mailchimp", "Google Analytics", "SEO", "SEM", "Content Marketing", "Social Media Marketing",
    "Email Marketing", "Copywriting", "Graphic Design", "Adobe Photoshop", "Adobe Illustrator", "Adobe InDesign", "Sketch", "Figma", "UI/UX Design", "User Research",
    "Wireframing", "Prototyping", "Product Management", "Agile", "Scrum", "Kanban", "Lean", "Project Management", "PMP", "PRINCE2",
    "Risk Management", "Business Analysis", "Data Analysis", "Data Visualization", "Statistical Analysis", "Machine Learning", "Deep Learning", "Natural Language Processing", "Computer Vision", "Data Mining",
    "Big Data", "Hadoop", "Spark", "Kafka", "NoSQL", "MongoDB", "Cassandra", "Redis", "Neo4j", "Blockchain",
    "Smart Contracts", "Cryptography", "Cybersecurity", "Penetration Testing", "Ethical Hacking", "Network Security", "Information Security", "Cloud Security", "IoT", "Embedded Systems",
    "Arduino", "Raspberry Pi", "VHDL", "Verilog", "FPGA", "ASIC Design", "Digital Signal Processing", "Robotics", "Automation", "Control Systems",
    "MATLAB", "Simulink", "LabVIEW", "ANSYS", "SolidWorks", "AutoCAD", "Revit", "BIM", "Civil Engineering", "Structural Engineering",
    "Mechanical Engineering", "Electrical Engineering", "Chemical Engineering", "Biotechnology", "Pharmaceuticals", "Healthcare", "Nursing", "Patient Care", "Clinical Research", "Medical Devices",
    "Regulatory Affairs", "Quality Assurance", "Six Sigma", "Lean Manufacturing", "Supply Chain Management", "Logistics", "Procurement", "Inventory Management", "Warehouse Management", "Transportation",
    "Fleet Management", "Vendor Management", "Customer Service", "Technical Support", "Help Desk", "ITIL", "COBIT", "TOGAF", "Enterprise Architecture", "Business Intelligence",
    "ETL", "Data Warehousing", "Data Governance", "Master Data Management", "Data Quality", "R", "SAS", "SPSS", "STATA", "JMP",
    "Minitab", "Python for Data Science", "R for Data Science", "SQL for Data Science", "Excel", "Advanced Excel", "Google Sheets", "Financial Analysis", "Accounting", "Auditing",
    "Taxation", "Budgeting", "Forecasting", "Financial Reporting", "Financial Modeling", "Investment Banking", "Equity Research", "Portfolio Management", "Risk Management", "Compliance",
    "AML", "KYC", "Credit Analysis", "Commercial Banking", "Retail Banking", "Insurance", "Actuarial Science", "Underwriting", "Claims Management", "Real Estate",
    "Property Management", "Facilities Management", "Construction Management", "Urban Planning", "Environmental Science", "Sustainability", "Renewable Energy", "Energy Management", "Oil & Gas", "Mining",
    "Geology", "Geophysics", "Geospatial Analysis", "GIS", "Remote Sensing", "Cartography", "Meteorology", "Climate Science", "Agriculture", "Horticulture",
    "Forestry", "Wildlife Conservation", "Marine Biology", "Oceanography", "Fisheries", "Aquaculture", "Veterinary Medicine", "Animal Husbandry", "Dairy Science", "Food Science",
    "Nutrition", "Dietitian", "Public Health", "Epidemiology", "Global Health", "Health Informatics", "Medical Coding", "Health Information Management", "Healthcare Administration", "Pharmacy",
    "Pharmacology", "Toxicology", "Clinical Trials", "GMP", "GLP", "GDP", "Pharmaceutical Manufacturing", "Biopharmaceuticals", "Bioprocessing", "Cell Culture",
    "Protein Purification", "Genomics", "Proteomics", "Metabolomics", "Bioinformatics", "Computational Biology", "Synthetic Biology", "Systems Biology", "Molecular Biology", "Cell Biology",
    "Microbiology", "Immunology", "Virology", "Pathology", "Histology", "Anatomy", "Physiology", "Biochemistry", "Neuroscience", "Psychology",
    "Cognitive Science", "Behavioral Science", "Social Work", "Sociology", "Anthropology", "Archaeology", "History", "Political Science", "International Relations", "Economics",
    "Macroeconomics", "Microeconomics", "Development Economics", "Health Economics", "Labor Economics", "Public Policy", "Public Administration", "Law", "Legal Research", "Legal Writing",
    "Contract Law", "Intellectual Property", "Patent Law", "Corporate Law", "Criminal Law", "Family Law", "Environmental Law", "Human Rights", "International Law", "Dispute Resolution",
    "Mediation", "Arbitration", "Litigation", "Tax Law", "Real Estate Law", "Employment Law", "Compliance", "Regulatory Affairs", "Corporate Governance", "Internal Audit",
    "Fraud Detection", "Forensic Accounting", "Cyber Law", "Privacy Law", "Data Protection", "IT Compliance", "Legal Compliance", "Regulatory Compliance", "AML Compliance", "KYC Compliance",
    "Risk Assessment", "Risk Mitigation", "Business Continuity", "Disaster Recovery", "Crisis Management", "Emergency Management", "Incident Management", "Change Management", "Organizational Development", "Talent Management",
    "Performance Management", "Compensation & Benefits", "Employee Engagement", "Training & Development", "HR Analytics", "Workforce Planning", "Recruitment", "Onboarding", "Employee Relations", "Labor Relations",
    "Industrial Relations", "Conflict Resolution", "Diversity & Inclusion", "Occupational Health & Safety", "Employee Wellness", "HRIS", "Payroll", "Benefits Administration", "Time & Attendance", "HR Policy",
    "HR Strategy", "HR Compliance", "HR Auditing", "HR Metrics", "HR Reporting", "HR Forecasting", "HR Budgeting", "HR Project Management", "HR Consulting", "Executive Coaching",
    "Leadership Development", "Succession Planning", "Career Development", "Talent Acquisition", "Executive Search", "Outplacement", "Employee Retention", "Employee Recognition", "Organizational Culture", "Organizational Change",
    "Organizational Effectiveness", "Organizational Leadership", "Organizational Design", "Organizational Behavior", "Employee Motivation", "Employee Satisfaction", "Employee Productivity", "Employee Performance", "Employee Training", "Employee Education",
    "Employee Communication", "Employee Feedback", "Employee Coaching", "Employee Counseling", "Employee Mentoring", "Employee Support", "Employee Assistance", "Employee Empowerment", "Employee Development", "Employee Growth",
    "Employee Advancement", "Employee Engagement Strategies", "Employee Experience", "Employee Lifecycle", "Employee Relations Strategies", "Employee Satisfaction Surveys", "Employee Wellbeing", "Employee Wellness Programs", "HR Analytics & Metrics", "HR Technology",
    "HR Transformation", "Human Capital Management", "Human Resources Planning", "Human Resources Strategy", "Performance Appraisal", "Performance Improvement", "Talent Development", "Talent Management Strategies", "Workforce Analytics", "Workforce Development",
    "Workforce Management", "Workforce Optimization", "Workforce Planning Strategies", "Workforce Productivity", "Workforce Retention", "Workforce Training", "Workplace Culture", "Workplace Diversity", "Workplace Inclusion", "Workplace Learning",
    "Workplace Safety", "Workplace Wellness", "Ad Operations", "Advertising", "Advertising Campaigns", "Advertising Sales", "Brand Management", "Brand Strategy", "Content Creation", "Content Development",
    "Content Management", "Creative Direction", "Digital Advertising", "Digital Marketing", "Event Management", "Experiential Marketing", "Market Analysis", "Market Research", "Marketing Communications", "Marketing Management",
    "Marketing Strategy", "Media Planning", "Media Relations", "Mobile Marketing", "Online Advertising", "Online Marketing", "PR Campaigns", "Product Marketing", "Public Relations", "SEO Strategy",
    "Social Media Advertising", "Social Media Management", "Strategic Communications", "Video Marketing", "Visual Merchandising", "Advertising Analytics", "Advertising Strategy", "Affiliate Marketing", "Brand Advertising", "Brand Awareness",
    "Brand Identity", "Brand Positioning", "Brand Promotion", "Business Development", "Channel Marketing", "Competitive Analysis", "Content Marketing Strategy", "Conversion Rate Optimization", "Creative Strategy", "Customer Acquisition",
    "Customer Insights", "Customer Journey", "Customer Retention", "Customer Segmentation", "Customer Targeting", "Direct Marketing", "Digital Content", "Digital Media", "Digital Strategy", "Display Advertising",
    "Email Campaigns", "Event Planning", "Influencer Marketing", "Integrated Marketing", "Lead Generation", "Marketing Automation", "Marketing Campaigns", "Marketing Channels", "Marketing Collateral", "Marketing Copywriting",
    "Marketing Data Analysis", "Marketing Insights", "Marketing Metrics", "Marketing Operations", "Marketing Plans", "Marketing Programs", "Marketing Research", "Marketing Technology", "Marketing Tools", "Media Buying",
    "Media Strategy", "Mobile Advertising", "Multichannel Marketing", "Omnichannel Marketing", "Online Campaigns", "Performance Marketing", "Product Launch", "Product Positioning", "Product Promotion", "Sales & Marketing",
    "Sales Enablement", "Sales Funnel", "Sales Planning", "Sales Strategies", "Search Engine Marketing", "Search Engine Optimization", "Social Media Campaigns", "Social Media Content", "Social Media Strategy", "Strategic Marketing",
    "Target Audience", "Target Marketing", "Trade Marketing", "Web Analytics", "Web Marketing", "Account Based Marketing", "Advertising Creative", "Advertising Management", "Advertising Production", "Brand Activation",
    "Brand Architecture", "Brand Equity", "Brand Experience", "Brand Loyalty", "Brand Management Strategy", "Brand Messaging", "Brand Metrics", "Brand Storytelling", "Brand Tracking", "Branded Content",
    "Campaign Analytics", "Campaign Management", "Campaign Optimization", "Cause Marketing", "Client Management", "Client Relations", "Community Management", "Consumer Behavior", "Consumer Insights", "Consumer Research",
    "Content Distribution", "Content Marketing Analytics", "Content Marketing Management", "Content Marketing Tools", "Content Promotion", "Content Strategy Development", "Conversion Optimization", "Creative Campaigns", "Creative Content", "Creative Development",
    "Customer Acquisition Strategies", "Customer Data Analytics", "Customer Experience Management", "Customer Insights Analysis", "Customer Interaction", "Customer Lifecycle Management", "Customer Loyalty Programs", "Customer Relationship Management", "Customer Retention Strategies", "Customer Satisfaction Analysis",
    "Customer Value Management", "Data Driven Marketing", "Data Interpretation", "Digital Advertising Campaigns", "Digital Content Creation", "Digital Content Strategy", "Digital Customer Experience", "Digital Innovation", "Digital Performance", "Digital Platform Management",
    "Digital Product Management", "Digital Project Management", "Digital Transformation Strategy", "E-commerce Marketing", "Email Marketing Automation", "Email Marketing Strategy", "Engagement Marketing", "Experiential Campaigns", "Field Marketing", "Global Marketing",
    "Influencer Outreach", "Innovation Marketing", "Integrated Campaigns", "International Marketing", "Lead Nurturing", "Loyalty Marketing", "Marketing Analysis & Insights", "Marketing Analytics Tools", "Marketing Budgeting", "Marketing Cloud",
    "Marketing Data Insights", "Marketing Data Strategy", "Marketing Execution", "Marketing Funnel", "Marketing Goals", "Marketing Intelligence", "Marketing Investment", "Marketing Measurement", "Marketing Optimization", "Marketing Orchestration",
    "Marketing Performance Management", "Marketing Plans Development", "Marketing Processes", "Marketing ROI", "Marketing Science", "Marketing Solutions", "Marketing Strategy Planning", "Marketing Tactics", "Marketing Trends", "Multichannel Campaigns",
    "Omnichannel Customer Experience", "Omnichannel Retail", "Online Customer Experience", "Online Marketing Campaigns", "Paid Media", "Partner Marketing", "Performance Advertising", "Personalization Strategy", "Product Development & Marketing", "Programmatic Advertising",
    "Promotion Strategy", "Public Relations Management", "Real-Time Marketing", "Referral Marketing", "Relationship Marketing", "Retail Marketing", "SEO & SEM", "SEO Copywriting", "Social Advertising", "Social Media Advertising Strategy",
    "Social Media Content Creation", "Social Media Management Tools", "Social Media Monitoring", "Social Media Optimization", "Social Media Planning", "Social Media Platforms", "Social Media Trends", "Strategic Branding", "Targeted Marketing Campaigns", "Video Content Strategy",
    "Video Production", "Viral Marketing", "Web Campaigns", "Web Content Creation", "Web Content Management", "Webinar Marketing", "Account Management", "Administrative Support", "Advanced Microsoft Office", "Asset Management",
    "Back Office Operations", "Banking Operations", "Bookkeeping", "Business Administration", "Business Analysis & Reporting", "Business Compliance", "Business Consulting", "Business Documentation", "Business Operations", "Business Process Improvement",
    "Client Services", "Compliance Audits", "Customer Operations", "Data Entry", "Data Management", "Data Processing", "Document Management", "Executive Administration", "Financial Administration", "Financial Operations",
    "Front Office Operations", "General Administration", "Internal Controls", "Inventory Control", "Office Administration", "Office Management", "Operations Coordination", "Operations Management", "Order Processing", "Payroll Management",
    "Process Management", "Project Coordination", "Quality Management", "Records Management", "Regulatory Compliance Management", "Retail Operations", "Risk Management Strategies", "Sales Administration", "Sales Operations", "Scheduling",
    "Supply Chain Operations", "Technical Documentation", "Technical Writing", "Telecommunications Operations", "Trade Compliance", "Transaction Processing", "Vendor Coordination", "Vendor Relations", "Virtual Assistant", "Workforce Management",
    "Workplace Administration", "Workplace Safety Management", "Administrative Assistance", "Advisory Services", "Automation Tools", "Business Continuity Management", "Business Processes", "Business Resilience", "Business Services", "Change Control",
    "Change Management Strategies", "Client Onboarding", "Client Retention Strategies", "Compliance & Regulations", "Cost Management", "Customer Experience Strategies", "Customer Relationship Strategies", "Data Administration", "Data Governance Strategies", "Data Integrity",
    "Data Privacy", "Data Protection Compliance", "Database Administration", "Database Management", "Document Control", "Document Production", "Document Review", "Executive Support", "Facility Management", "Financial Compliance",
    "Financial Operations Management", "HR Operations", "Information Security Compliance", "IT Administration", "IT Operations", "IT Service Management", "Operational Efficiencies", "Operational Excellence", "Operational Improvements", "Operations Optimization",
    "Organizational Processes", "People Operations", "Procurement Management", "Productivity Management", "Records Compliance", "Regulatory Compliance Strategies", "Risk Assessment Strategies", "Risk Mitigation Strategies", "Safety Compliance", "Service Management",
    "Staff Coordination", "Staff Operations", "System Administration", "Systems Compliance", "Team Coordination", "Time Management Tools", "Transaction Management", "Vendor Management Strategies", "Workflow Management", "Workplace Efficiency"
]
print(len(candidate_skills))
print(datetime.now())
print('Generate embeddings started')
# Generate embeddings
job_embeddings = model.encode(job_skills, convert_to_tensor=True)
candidate_embeddings = model.encode(candidate_skills, convert_to_tensor=True)
print(candidate_embeddings)
print('Generate embeddings ended')
print('scores calculation started')
print(datetime.now())
# Calculate similarity scores
similarity_matrix = util.pytorch_cos_sim(candidate_embeddings, job_embeddings)
print('scores calculation ended')
# Display similarity scores using pandas DataFrame
df_similarity = pd.DataFrame(similarity_matrix.cpu().numpy(), columns=job_skills, index=candidate_skills)

# Print and display DataFrame
print("\nBERT Similarity:")
print(df_similarity)
print(datetime.now())
