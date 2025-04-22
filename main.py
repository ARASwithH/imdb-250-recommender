import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier

# opening file
with open('dirty_datas.csv', 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    dirty_datas = dict(csv_reader)

# making a list of plot summaries
text = [dirty_datas[i] for i in dirty_datas]

# making an instance of functions
tfidf_vectorizer = TfidfVectorizer(max_df=1.0, min_df=1, stop_words='english', norm=None)

# making a matrix of tf_idf
tfidf_matrix = tfidf_vectorizer.fit_transform(text)

# making an instance of functions
knn = KNeighborsClassifier(n_neighbors=6, metric='cosine')

# calculating KNN
knn.fit(tfidf_matrix, range(len(text)))

# get input
input_summary = input('Please input the summary: ')

# vectorizing input
input_vector = tfidf_vectorizer.transform([input_summary])

# getting top 5 movies
distances, indices = knn.kneighbors(input_vector, n_neighbors=6)

for k in indices.tolist()[0][1:]:
    for i, j in enumerate(dirty_datas):
        if i == k:
            print(f'{i} , {j}')
