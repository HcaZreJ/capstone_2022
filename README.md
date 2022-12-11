## Notes:
* Most of the work done since the "Mid-Term Deliverable assignment" can be found in the  __test.ipynb__  notebook, which went through the entire process of web-crawling, news article data cleaning, pre-trained Google-news Word2Vec model load-in, news-to-vector transformation, user-preference learning, and prediction generation.
* Web app deployment is attempted but encountered two major roadblocks:
  * It will 100% cost money and quite expensive if faster computational speed is required
  * There's a lot of new stuff to learn, and I am still trying to figure out how to get things up and running, and how to get them to communicate with each other.
* I am leaning towards putting money onto this project (unless there is a free way to get a web app up and running because I did not find any), because I think it will be a project that looks good on my resume, in addition I do not think theoretical analysis is my thing (i.e. making a pivot and turning the project into a theoretical analysis paper)

# Capstone 2022

[![LinkedIn][linkedin-shield]][linkedin-url]

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

Capstone Project of Data Science major student Zichen Zhu at Minerva University. The goal of the project is to develop a web app that will be
able to give personalized news recommendations. The central idea of the project is that news articles can be converted into vectors using some
Word2Vec model, which captures the semantic difference between them. Then if we learn the preference of users on the same semantic dimensions by asking them to rate how interested they are with several news articles, we will be able to generate personalized news recommendations by looking for news article vectors that is close to the preference vector of the user.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the
acknowledgements section. Here are a few examples.

* [<img width="184" alt="截屏2022-12-11 15 44 00" src="https://user-images.githubusercontent.com/77333293/206892061-85b0876d-aea0-4522-97f5-5a9a1968e6db.png">](https://newsapi.org/)
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

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

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

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members

[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers

[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues

[license-shield]: https://img.shields.io/github/license/HcaZreJ/capstone_2022
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew


