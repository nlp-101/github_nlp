# NLP Project

May 13, 2019

## Authors
> Cody Watson -- Codeup Student  
> Eric Escalante -- Codeup Student  

For this project, we will be scraping data from GitHub repository README files. The goal is to build a model that can predict which programming language a repository is using, given the text of the README file.  


![alt text][logo1]

[logo1]: https://media.giphy.com/media/TFNLyTG6CS8OwMCods/giphy.gif "Word Clouds"


Rejects non-ascii README files(i.e. foriegn languages)

Classification Models Used:
- Logistic Regression
- Decision Tree (Best Train Model)
- Random Forest
- KNN

Link to our Google Doc slides:
https://docs.google.com/presentation/d/140kq1B3q0hpaq6hiGjjg7N2KYmLHYG8EalrxAUBPkcs/edit?usp=sharing

Our visuals and ML models can be found on NLP_Projects.ipynb

![alt text][logo]

[logo]: https://github.com/nlp-101/github_nlp/blob/master/images/Screen%20Shot%202019-05-13%20at%2011.58.39%20AM.png "Full Corpus Word Web"

**Full Corpus Word Web:** We used the top 20 words in each language to build a word network. Each programming language contains certain unique words and words that are common in multiple languages. The Network shows the programming language as a unique node and the edges show the word relationship between the languages. From here we can answer the questions above.
