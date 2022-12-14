<a name="readme-top"></a>

## Notes:
* Most of the work done since the "Mid-Term Deliverable assignment" can be found in the  __test.ipynb__  notebook, which went through the entire process of web-crawling, news article data cleaning, pre-trained Google-news Word2Vec model load-in, news-to-vector transformation, user-preference learning, and prediction generation. 
  * Important functions such as data cleaning, news-to-vector transformation are packaged into functions that can be copy-pasted and used anywhere.
  * This means that although the application is not deployed because I have not figured it out fully, it is deployment-ready by simply copy-pasting the functions I've defined.
  * The test.ipynb file is the project tested out locally. It is the main thing that is new and what I'm handing in for grading for the Full Draft. Other surrounding documents handed-in include this GitHub README document, updated Notion page (roadmap/process), and the HC&LO justification tables on the Notion page.
* Web app deployment is attempted but encountered two major roadblocks:
  * It will 100% cost money and it will be quite expensive. The pre-trained GoogleNews model is 3.64GB on disk which forces one to buy an expensive one, because the model needs to be in RAM when the model is ran (so you need a server that has like at the very least 8GB of RAM).
  * There's a lot of new stuff to learn, and I am still trying to figure out how to get things up and running, and how to get them to communicate with each other.
* I am leaning towards putting money onto this project (unless there is a free way to get a web app up and running because I did not find any), because I think it will be a project that looks good on my resume, in addition I do not think theoretical analysis is my thing (i.e. making a pivot and turning the project into a theoretical analysis paper)
* Feedback requested:
  * How do I get this thing deployed so that I can gather feedback from people? Is there anyway that I could get this thing deployed without spending money on it? The problem is that I cannot send the entire .ipynb notebook to people, ask them to download Python, install all of the packages necessary for the code to run, then run the notebook for 30 minutes just to get a few not so useful news article recommendations to read. On the other side, deploying off the internet is 100% going to cost money.
  * Anything you think will be worthy for me to read into / learn about to make this project achieve its goal better: give users personalized news recommendation.
  * HC&LO justifications. Please give comments on whether they would be applications that deserves a 4. If not, how can I improve them so that I can get a 4?
* Summary of feedbacks applied:
  * All feedbacks on HC&LO justifications are moved to the comment section of the respective HC&LO's page and acted upon. Most justifications have been updated and changes are marked with a blue color.
  * Please check the "Feedback Received" section of the Notion page for all of the feedback that has been acted upon, which is marked out with a blue color and/or has a :white_check_mark: in front. To name a few:
    * Web-scraping was conducted first, which is fully functional now and building up a dataset.
    * Pre-trained Word-embedding model (Google News Word2Vec) is used for this first iteration of the product to speed up the development process as suggested.
    * Representation of the dataset is now clear - News articles are all stored as vectors, converted using the Google News Word2Vec model. In addition a similarity matrix is created that makes cross-comparison between articles much faster.


<!-- PROJECT SHIELDS -->
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
 <!-- ADD A PROJECT IMAGE HERE LATER ONCE THERE IS ONE
  <a href="https://github.com/HcaZreJ/capstone_2022">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>
 -->

  <h1 align="center">Personalized News Recommender</h1>

  <p align="center">
    Gives personalized news recommendations after learning your news preference by asking you to rate 10 news articles.
    <br />
    <a href="https://github.com/HcaZreJ/capstone_2022"><strong>Explore the docs ??</strong></a>
    <br />
    <br />
    <a href="https://github.com/HcaZreJ/capstone_2022">View Demo</a>
    ??
    <a href="https://github.com/HcaZreJ/capstone_2022/issues">Report Bug</a>
    ??
    <a href="https://github.com/HcaZreJ/capstone_2022/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## About The Project

Capstone Project of Data Science major student Zichen Zhu at Minerva University. The goal of the project is to develop a web app that will be able to give personalized news recommendations. News articles will be converted into vectors using some Word2Vec model, which captures the semantic difference between them. Then if we learn the preference of users on the same semantic dimensions by asking them to rate how interested they are with several news articles, we will be able to generate personalized news recommendations by looking for news article vectors that is close to the preference vector of the user.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the
acknowledgements section. Here are a few examples.

* [<img width="184" alt="??????2022-12-11 15 44 00" src="https://user-images.githubusercontent.com/77333293/206892061-85b0876d-aea0-4522-97f5-5a9a1968e6db.png">](https://newsapi.org/)
* [<img width="184" src="https://user-images.githubusercontent.com/77333293/206892313-9addec46-4c17-4eed-816a-3ff93367939f.png">](https://radimrehurek.com/gensim/)
* [<img width="184" src="https://user-images.githubusercontent.com/77333293/206893467-b8d22065-66cb-48fa-92c6-c9df57dcf48e.png">](https://numpy.org/)
* [<img width="184" src="https://user-images.githubusercontent.com/77333293/206893469-d4f97224-0401-4ad2-b2b3-1498faa25e8b.png">](https://pandas.pydata.org/)
* [<img width="184" src="https://user-images.githubusercontent.com/77333293/206894090-fd5dba0f-1731-47a5-bb70-71c0715238c6.png">](https://scikit-learn.org/stable/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

To run the test.ipynb file locally, you must have Python 3.9.10 locally, then setup your environment following the steps below:

### Prerequisites

Install the following packages into your local Python environment, by typing the following commands in your command line (Note: you might need to add <code>python -m</code> in front if you do not have pip in your base path):
* NumPy
  ```sh
  pip install numpy
  ```
* pandas
  ```sh
  pip install pandas
  ```
* Beautiful Soup
  ```sh
  pip install beautifulsoup4
  ```
* contractions
  ```sh
  pip install contractions
  ```
* The Natural Language Toolkit (NLTK)
  ```sh
  pip install nltk
  ```
* Gensim
  ```sh
  pip install --upgrade gensim
  ```
* scikit-learn
  ```
  pip install -U scikit-learn
  ```

### Newsapi

The program includes sending requests to the Newsapi website to obtain recent news article links, if you used mine in the ipynb notebook, it might return no results because I registered for a free developer's account that is limited to 200 requests per day. It is recommended that you register your own free Newsapi account and supply it to the notebook before running it. Here are the steps:

1. Get a free API Key at [https://newsapi.org/](https://newsapi.org/)
2. Enter your API Key at the top of the test.ipynb notebook
   ```py
   apiKey = 'ENTER YOUR API Key'
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Google News Word2Vec

The program also uses a pre-trained Google News Word2Vec model that is 3.64GB on disk and stored in a binary file format. Before running the program, you would need to download the binary file, and store it under the same directory as the test.ipynb file.

Documentation for pre-trained Google Word2Vec models can be found [here](https://code.google.com/archive/p/word2vec/), whereas the Google News Word2Vec model's binary file can be downloaded [here](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?resourcekey=0-wjGZdNAUop6WykTtMip30g).


## Usage

(Section not yet updated, left the template here to be used in the future)

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

(Section not yet updated, left the template here to be used in the future)

- [x] Add Changelog
- [x] Add back to top links
- [ ] Add Additional Templates w/ Examples
- [ ] Add "components" document to easily copy & paste sections of the readme
- [ ] Multi-language Support
    - [ ] Chinese
    - [ ] Spanish

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Zichen Zhu - zachzhu@uni.minerva.edu

Project Link: [https://github.com/HcaZreJ/capstone_2022](https://github.com/HcaZreJ/capstone_2022)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Readme Template used](https://github.com/othneildrew/Best-README-Template)
* [GitHub Markdown Emojis :stuck_out_tongue_closed_eyes:](https://gist.github.com/rxaviers/7360908)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[license-shield]: https://img.shields.io/github/license/HcaZreJ/capstone_2022?style=for-the-badge
[license-url]: https://github.com/HcaZreJ/capstone_2022/blob/main/LICENSE.txt

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-blue.svg?style=for-the-badge&logo=linkedin
[linkedin-url]: https://www.linkedin.com/in/zichen-zhu-6695b7173/


