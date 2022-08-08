import streamlit as st
from google.cloud import firestore

# Authenticating to Firestore with the JSON account key.
db = firestore.Client.from_service_account_json("firestore-key.json")

# Create a refernce to the Google post.

doc_ref = db.collection("posts").document("Google")

# Then get the data at that reference.
doc = doc_ref.get()

# Let's see what we got!
st.write("The id is: ",doc.id)
st.write("The contents are: ", doc.to_dict())

doc_ref = db.collection("posts").document("Apple")

doc_ref.set({
    "title": "Apple",
    "url": "www.apple.com"
})

posts_ref = db.collection("posts")

for doc in posts_ref.stream():
    st.write("The id is: ", doc.id)
    st.write("The contents are: ", doc.to_dict())