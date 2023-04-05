<a name="readme-top"></a>

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
    <a href="https://github.com/HcaZreJ/capstone_2022"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/HcaZreJ/capstone_2022">View Demo</a>
    ·
    <a href="https://github.com/HcaZreJ/capstone_2022/issues">Report Bug</a>
    ·
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

Capstone Project of Data Science major student Zichen Zhu at Minerva University. The goal of the project is to develop a web app that will be able to give personalized news recommendations. News articles are converted into vector representations, by transforming the headline of the article using the Google Universal Sentence Encoder(GUSE) model, which captures the semantic difference across sentences. Then we can add another probability density dimension on top of the semantic dimensions provided by GUSE, and learn the preference of the user by building normal distributions around the articles that the user claims to be interested in, adjusted based on the rating that the user gave to the article. Subsequently we can generate personalized news recommendations to the user just by sampling from this probability density function.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the
acknowledgements section. Here are a few examples.

- [<img width="184" alt="截屏2022-12-11 15 44 00" src="https://user-images.githubusercontent.com/77333293/206892061-85b0876d-aea0-4522-97f5-5a9a1968e6db.png">](https://newsapi.org/)
- [<img width="184" src="https://user-images.githubusercontent.com/77333293/206892313-9addec46-4c17-4eed-816a-3ff93367939f.png">](https://radimrehurek.com/gensim/)
- [<img width="184" src="https://user-images.githubusercontent.com/77333293/206893467-b8d22065-66cb-48fa-92c6-c9df57dcf48e.png">](https://numpy.org/)
- [<img width="184" src="https://user-images.githubusercontent.com/77333293/206893469-d4f97224-0401-4ad2-b2b3-1498faa25e8b.png">](https://pandas.pydata.org/)
- [<img width="184" src="https://user-images.githubusercontent.com/77333293/206894090-fd5dba0f-1731-47a5-bb70-71c0715238c6.png">](https://scikit-learn.org/stable/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

To check out a low-end beta version of this web app, visit: https://colab.research.google.com/drive/1R9tvOwg35IeKIdiRJV9KJlMK0YSKWQRp?usp=sharing

To run the web app locally, you must have Python 3.9.10 locally, then setup your environment following the steps below:

"<"TO BE COMPLETED">"

### Prerequisites

Install the following packages into your local Python environment, by typing the following commands in your command line (Note: you might need to add <code>python -m</code> in front if you do not have pip in your base path):

- NumPy
  ```sh
  pip install numpy
  ```
- pandas
  ```sh
  pip install pandas
  ```
- Beautiful Soup
  ```sh
  pip install beautifulsoup4
  ```
- contractions
  ```sh
  pip install contractions
  ```
- The Natural Language Toolkit (NLTK)
  ```sh
  pip install nltk
  ```
- Gensim
  ```sh
  pip install --upgrade gensim
  ```
- scikit-learn
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

### Google Universal Sentence Encoder

The program also uses a pre-trained Google Universal Sentence Encoder model that is 1.04GB on disk and stored in a folder format. Before running the program, you would need to download the zipped folder, and store it under the same directory as the news_to_vector_v2.py file. The one that is one this GitHub Repo is managed by Git LFS, which might not come along with all of the others if you forked this repo.

Documentation & downloading for pre-trained Google Universal Sentence Encoder can be found [here](https://tfhub.dev/google/universal-sentence-encoder/4).

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

- [Readme Template](https://github.com/othneildrew/Best-README-Template)
- [GitHub Markdown Emojis :stuck_out_tongue_closed_eyes:](https://gist.github.com/rxaviers/7360908)
- [Tutorial on Flask website building](https://www.youtube.com/watch?v=dam0GPOAvVI)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[license-shield]: https://img.shields.io/github/license/HcaZreJ/capstone_2022?style=for-the-badge
[license-url]: https://github.com/HcaZreJ/capstone_2022/blob/main/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-blue.svg?style=for-the-badge&logo=linkedin
[linkedin-url]: https://www.linkedin.com/in/zichen-zhu-6695b7173/
