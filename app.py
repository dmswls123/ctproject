import streamlit as st
import pandas as pd
# import plotly.figure_factory as ff
import plotly.express as px
# import matplotlib.pyplot as pit


# global variable
url ="https://www.youtube.com/watch?v=XyEOEBsa8I4"

# data app
df = pd.read_csv('./data/data.csv')
filehtml = pd.read_html('./com_html.html')

st.set_page_config(layout='wide', page_title='My App')

# html variable
html = '''
<html>
    <head>
        <title>This is HTML App</title>
    </head>
    <body>
        <h1>This Long Text!!!</h1>
        <hr>
        <hr>
        <h3>This a small text</h3>
    </body>
</html>
'''

st.title('EUnjin first webapp!')
col1, col2 = st.columns((4,1))
with col1:
    with st.expander('Content1...'):
        st.subheader('Content1...')
        st.video(url)
    
    with st.expander('Content2...'):
        st.subheader('Content2...')
        st.table(df)
        #dff=df.groupby(by='name').sum()
        #st.table(dff)
        #st.plotly_chart(df)
        #fig = px.line(df, x=df.columns[0], y=df.columns[3], title='Plotly Chart')
        #st.plotly_chart(fig)

    with st.expander('Content3_images...'):
        st.subheader('Catdog image')
        st.image('./images/catdog.png')
        st.markdown(html, unsafe_allow_html=True)
        #st.write('<h1>This is new title</h1>', unsafe_allow_html=True)

    with st.expander('Content4_html...'):
        st.subheader('Content4_html...')
        import streamlit.components.v1 as htmlviewer
        htmlviewer.html(filehtml, height=800)

with col2:
    with st.expander('Tips...'):
        st.subheader('Tips...')