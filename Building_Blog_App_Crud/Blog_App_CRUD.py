# pip install streamlit
# streamlit run  app.py

# CRUD stands for Create, Read,Update and Delete. In our case we will be building a CRD app

# We will be using sqlite3 for our database management ,
# pandas and matplotlib for our  simple analytics or metrics and streamlit for everything else.

# pip install streamlit pandas matplotlib

'''

Main App: Our main app will consist of  5 sections

    Home: simple preview or list of all posts
    View Posts: where we will display  full articles to read
    Add Post: where we create our post
    Search: where we can search articles by title or author fields
    Manage Blog: where we will delete and check for our analytics.

Back-end DB Management: We will be using normal SQL and sqlite3 
for our  handling our database. For interacting with our database 
I'll create individual functions and utilize these functions 
within my app.

'''

# DataBase[DB]

import sqlite3
from turtle import pd

from wordcloud import WordCloud
conn = sqlite3.connect('data.db')
c = conn.cursor()

# Functions
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS blogtable(author TEXT,title TEXT,article TEXT,postdate DATE)')
    
def add_data(author, title, article, postdate):
    c.execute('INSERT INTO blogtable(author,title,article,postdate) VALUES (?,?,?,?)',(author,title,article,postdate))
    conn.commit()
    
def view_all_notes():
    c.execute('SELECT * FROM blogtable')
    data = c.fetchall()
    return data

def view_all_titles():
    c.execute('SELECT DISTINCT title FROM blogtable')
    data = c.fetchall()
    return data

def get_blog_by_title(title):
    c.execute('SELECT * FROM blogtable WHERE title="{}"'.format(title))
    data = c.fetchall()
    return data

def get_blog_by_author(author):
    c.execute('SELECT * FROM blogtable WHERE author="{}"'.format(author))
    data = c.fetchall()
    return data

def delete_data(title):
    c.execute('DELETE FROM blogtable WHERE title="{}"'.format(title))
    conn.commit()
    
'''

For my Home Section, I will display all the posts we are receiving from 
the user which was stored in the database.

'''

# Layout Templates
html_temp = """
<div style = "background-color:{};padding:10px;border-radius:10px">
<h1 style = "color:{};text-align:center;">Simple Blog Posts</h1>
</div>
"""   

title_temp = """
<div style="background-color:#464e5f;padding:10px;border-radius:10px;margin:10px;">
<h4 style ="color:white;text-align:centre;">{}</h1>
<img src = "https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;" >
<h6>Author:{}</h6>
<br/>
<br/>
<p style="text-align:justify">{}</p>
</div>
""" 

article_temp = """
<div style="background-color:#464e5f;padding:10px;border-radius:5px;margin:10px;">
<h4 style="color:white;text-align:center;">{}</h1>
<h6>Author:{}</h6>
<h6>Post Date: {}</h6>
<img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;width: 50px;height: 50px;border-radius: 50%;" >
<br/>
<br/>
<p style="text-align:justify">{}</p>
</div>
"""

head_message_temp ="""
<div style="background-color:#464e5f;padding:10px;border-radius:5px;margin:10px;">
<h4 style="color:white;text-align:center;">{}</h1>
<img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;">
<h6>Author:{}</h6> 
<h6>Post Date: {}</h6> 
</div>
"""

full_message_temp ="""
<div style="background-color:silver;overflow-x: auto; padding:10px;border-radius:5px;margin:10px;">
<p style="text-align:justify;color:black;padding:10px">{}</p>
</div>
"""

'''
- For our Add Post section we will use the normal st.text_input() 
and st.text_area() as well as the st.date_input() respectively.

- Since we cannot yet use nested routing in streamlit, we will 
create another section to view the entire post.

- For our Search Section we will utilize simple SQL query to fetch 
the data using two fields – title or author name.

- Finally for our Manage Blog Section we will add the ability to 
delete a blog and some simple plots for our analytics.

'''


from matplotlib import pyplot as plt
import streamlit as st

def main():
	"""A Simple CRUD  Blog"""
	
	st.markdown(html_temp.format('royalblue','white'),unsafe_allow_html=True)

	menu = ["Home","View Posts","Add Posts","Search","Manage Blog"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home")
		result = view_all_notes()
		
		for i in result:
			b_author = i[0]
			b_title = i[1]
			b_article = str(i[2])[0:30]
			b_post_date = i[3]
			st.markdown(title_temp.format(b_title,b_author,b_article,b_post_date),unsafe_allow_html=True)

	elif choice == "View Posts":
		st.subheader("View Articles")
		all_titles = [i[0] for i in view_all_titles()]
		postlist = st.sidebar.selectbox("View Posts",all_titles)
		post_result = get_blog_by_title(postlist)
		for i in post_result:
			b_author = i[0]
			b_title = i[1]
			b_article = i[2]
			b_post_date = i[3]
			st.text("Reading Time:{}".format(readingTime(b_article))) # type: ignore
			st.markdown(head_message_temp.format(b_title,b_author,b_post_date),unsafe_allow_html=True)
			st.markdown(full_message_temp.format(b_article),unsafe_allow_html=True)



	elif choice == "Add Posts":
		st.subheader("Add Articles")
		create_table()
		blog_author = st.text_input("Enter Author Name",max_chars=50)
		blog_title = st.text_input("Enter Post Title")
		blog_article = st.text_area("Post Article Here",height=200)
		blog_post_date = st.date_input("Date")
		if st.button("Add"):
			add_data(blog_author,blog_title,blog_article,blog_post_date)
			st.success("Post:{} saved".format(blog_title))	




	elif choice == "Search":
		st.subheader("Search Articles")
		search_term = st.text_input('Enter Search Term')
		search_choice = st.radio("Field to Search By",("title","author"))
		
		if st.button("Search"):

			if search_choice == "title":
				article_result = get_blog_by_title(search_term)
			elif search_choice == "author":
				article_result = get_blog_by_author(search_term)


			for i in article_result:
				b_author = i[0]
				b_title = i[1]
				b_article = i[2]
				b_post_date = i[3]
				st.text("Reading Time:{}".format(readingTime(b_article))) # type: ignore
				st.markdown(head_message_temp.format(b_title,b_author,b_post_date),unsafe_allow_html=True)
				st.markdown(full_message_temp.format(b_article),unsafe_allow_html=True)




	elif choice == "Manage Blog":
		st.subheader("Manage Articles")

		result = view_all_notes()
		clean_db = pd.DataFrame(result,columns=["Author","Title","Articles","Post Date"])
		st.dataframe(clean_db)

		unique_titles = [i[0] for i in view_all_titles()]
		delete_blog_by_title = st.selectbox("Unique Title",unique_titles)
		new_df = clean_db
		if st.button("Delete"):
			delete_data(delete_blog_by_title)
			st.warning("Deleted: '{}'".format(delete_blog_by_title))


		if st.checkbox("Metrics"):
			
			new_df['Length'] = new_df['Articles'].str.len()
			st.dataframe(new_df)


			st.subheader("Author Stats")
			new_df["Author"].value_counts().plot(kind='bar')
			st.pyplot()

			st.subheader("Author Stats")
			new_df['Author'].value_counts().plot.pie(autopct="%1.1f%%")
			st.pyplot()

		if st.checkbox("Word Cloud"):
			st.subheader("Generate Word Cloud")
			# text = new_df['Articles'].iloc[0]
			text = ','.join(new_df['Articles'])
			wordcloud = WordCloud().generate(text)
			plt.imshow(wordcloud,interpolation='bilinear')
			plt.axis("off")
			st.pyplot()

		if st.checkbox("BarH Plot"):
			st.subheader("Length of Articles")
			new_df = clean_db
			new_df['Length'] = new_df['Articles'].str.len()
			barh_plot = new_df.plot.barh(x='Author',y='Length',figsize=(20,10))
			st.pyplot()


if __name__ == '__main__':
	main()
