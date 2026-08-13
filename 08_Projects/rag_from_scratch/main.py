import math
import os
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
client = OpenAI()
api_key =os.getenv("OPENAI_API_KEY")
is_api_key_exists = api_key is not None and len(api_key) > 0
print(f"API key exists: {is_api_key_exists}")



documents = [
    "Employees receive 20 days of annual leave per year.",
    "Employees receive health insurance benefits, including medical, dental, and vision coverage.",
    "Employees can work remotely up to two days per week.",
    "Employees are eligible for a 401(k) retirement plan with company matching.",
    "Employees receive paid parental leave for up to 12 weeks."
]

document_embeddings = [[0.35, 0.12, 0.78, 0.45, 0.67],
                       [0.22, 0.55, 0.33, 0.44, 0.11],
                       [0.15, 0.88, 0.99, 0.22, 0.33],
                       [0.44, 0.66, 0.77, 0.88, 0.99],  
                       [0.11, 0.22, 0.33, 0.44, 0.55]]
print(document_embeddings[0])
print(document_embeddings[0][0])
print(len(document_embeddings[0]))


query = "How many vacation days do employees get?"
print(query)

query_embedding = [0.30, 0.10, 0.70, 0.40, 0.60]
print(query_embedding)


dot_product = sum(i*j for i,j in zip(query_embedding,document_embeddings[0]))
print(dot_product)


query_magnitude = math.sqrt(sum(x*x for x in query_embedding))

print(query_magnitude)

document_magnitude = math.sqrt(sum(x*x for x in document_embeddings[0]))

print(document_magnitude)

similarity = dot_product / (query_magnitude * document_magnitude)
print(similarity)


def cosine_similarity(vector_a,vector_b):
    dot_product = sum(i*j for i,j in zip(vector_a,vector_b))
    magnitude_a = math.sqrt(sum(x*x for x in vector_a))
    magnitude_b = math.sqrt(sum(x*x for x in vector_b))
    if magnitude_a == 0 or magnitude_b == 0:
        return 0
    return dot_product / (magnitude_a * magnitude_b)

similarity_score = cosine_similarity(query_embedding,document_embeddings[0])

print(similarity_score)


scores =[]
for document_embedding in document_embeddings:
    score=cosine_similarity(query_embedding, document_embedding)
    scores.append(score)

print(scores)


results = list(zip(documents,scores)) 

results.sort(key=lambda x:x[1], reverse=True)
print(results)

top_k=3
top_k_results=results[:top_k]
print(top_k_results)

retrieved_chunks = [chunk for chunk, score in top_k_results]
print(retrieved_chunks)


CONTEXT ="\n".join(retrieved_chunks)
print(CONTEXT)


prompt =f"""
Answer the question based on the context provided below.
Context: {CONTEXT}
Query: {query}
Answer:
"""

print(prompt)


response = client.embeddings.create(
    model="text-embedding-3-small",
    input=query
)




query_embedding_real = response.data[0].embedding
print(type(query_embedding_real))
print(len(query_embedding_real))   

query_embedding = query_embedding_real
print(len(query_embedding))

document_response =client.embeddings.create(
    model="text-embedding-3-small",
    input=documents
)

print(len(document_response.data))

document_embeddings_real = [item.embedding for item in document_response.data]
print(len(document_embeddings_real))
print(len(document_embeddings_real[0]))

document_embeddings = document_embeddings_real
print(len(document_embeddings))
print(len(document_embeddings[0]))

real_similarity_score = cosine_similarity(query_embedding,document_embeddings[0])
print(real_similarity_score)


real_scores =[]
for document_embedding in document_embeddings:
    score=cosine_similarity(query_embedding, document_embedding)
    real_scores.append(score)

print(real_scores)    


real_results =list(zip(documents,real_scores))
real_results.sort(key=lambda x:x[1], reverse=True)

top_k_real_results = real_results[:top_k]
print(top_k_real_results)


vector_store = list(zip(documents,document_embeddings))

print(vector_store[0][0])
print(len(vector_store[0][1])) 

scores=[]
for item in vector_store:
    similarity=cosine_similarity(query_embedding, item[1])
    scores.append((item[0], similarity))

print(scores)    

scores.sort(key=lambda x:x[1], reverse=True)
print(scores)

top_k_results = scores[:top_k]
print(top_k_results)



def retrieve(query_embedding,vector_store,top_k):
    scores=[]
    for item in vector_store:
        similarity=cosine_similarity(query_embedding, item[1])
        scores.append((item[0], similarity))
    scores.sort(key=lambda x:x[1], reverse=True)
    top_k_results = scores[:top_k]
    return top_k_results

top_k_results = retrieve(query_embedding,vector_store,2)
print(top_k_results)


retrieved_chunks = [chunk for chunk, score in top_k_results]
print(retrieved_chunks)

context = "\n".join(retrieved_chunks)
print(context)


def build_context(top_k_results):
    retrieved_chunks = [chunk for chunk, score in top_k_results]
    context = "\n".join(retrieved_chunks)
    return context

context = build_context(top_k_results)
print(context)



def generate_answer(query, context):
    prompt = f"""
    Answer the question based on the context provided below.
    Context: {context}
    Query: {query}
    Answer:
    """
    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )
    return response.output_text
response = generate_answer(query, context)
print(response)

