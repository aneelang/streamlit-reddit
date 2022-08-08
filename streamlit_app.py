import streamlit as st
from google.cloud import firestore

# Authenticating to Firestore with the JSON account key.
db = firestore.Client.from_service_account_json("firestore-key.json")

# import json
# key_dict = json.loads(st.secrets["textkey"])
# creds = service_account.Credentials.from_service_account_info(key_dict)
# db = firestore.Client(credentials = creds, project = "streamlit-reddit")

# Create a refernce to the Google post.

doc_ref = db.collection("posts").document("Google")

# # Then get the data at that reference.
# doc = doc_ref.get()

# # Let's see what we got!
# st.write("The id is: ",doc.id)
# st.write("The contents are: ", doc.to_dict())

# doc_ref = db.collection("posts").document("Apple")

# doc_ref.set({
#     "title": "Apple",
#     "url": "www.apple.com"
# })

# posts_ref = db.collection("posts")

# for doc in posts_ref.stream():
#     st.write("The id is: ", doc.id)
#     st.write("The contents are: ", doc.to_dict())

title = st.text_input("Post title")
url = st.text_input("Post url")
submit = st.button("Submit new post")

if title and url and submit:
    doc_ref = db.collection("posts").document(title)
    doc_ref.set({
        "title": title,
        "url": url
    })

posts_ref = db.collection("posts")

for doc in posts_ref.stream():
    post = doc.to_dict()
    title = post["title"]
    url = post["url"]

    st.subheader(f"Post: {title}")
    st.write(f":link:[{url}]")