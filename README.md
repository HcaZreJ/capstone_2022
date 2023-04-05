<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->

[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- Headers -->
<div align="center">

  <h1 align="center">Personalized News Recommender</h1>

  <p align="center">
    News Recommendations tailored to your preference, for efficient news reading.
    <br />
    <!--
    <a href="https://github.com/HcaZreJ/capstone_2022">View Demo</a>
    ·-->
    <a href="https://colab.research.google.com/drive/1R9tvOwg35IeKIdiRJV9KJlMK0YSKWQRp?usp=s%20haring#scrollTo=F2rhdN40r4Tq">Colab Version</a>
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
        <li><a href="#news-api">News API</a></li>
        <li><a href="#google-universal-sentence-encoder">Google Universal Sentence Encoder</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## About The Project

Capstone Project of Data Science major student Zichen Zhu at Minerva University. The goal of the project is to develop a product that will help myself read news more efficiently.

Initially, I intended to create a Flask web app that will be deployed and widely accessible. However, I later realized that the Sentence Encoder I used is too big, and it will cost money to be deployed. So instead here is the web app's code that can be downloaded and deployed locally using Flask.

The web app allows you to create an account and enjoy news recommendations personalized to your preference. Upon sign up, the web app will ask you to rate 6 articles, on a scale of 0 to 5, with 0 being "I do not want to see this at all" up to 5 being "I want to see this all the time." This gives the app an initial capture of your preference, then on subsequent log in, you will see 6 news recommendations tailored to your preference, which you can also rate to help the app improve.

To see how this works, navigate to the top and click on "View Demo".

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

Here are the major frameworks and libraries used to build this project.

- [<img width="184" alt="截屏2022-12-11 15 44 00" src="https://user-images.githubusercontent.com/77333293/206892061-85b0876d-aea0-4522-97f5-5a9a1968e6db.png">](https://newsapi.org/)
- [<img width="184" src="https://user-images.githubusercontent.com/77333293/230166191-39767201-baca-45af-9eff-afbf408cf7c3.png">](https://tfhub.dev/google/universal-sentence-encoder/4)
- [<img width="184" src="https://user-images.githubusercontent.com/77333293/206893467-b8d22065-66cb-48fa-92c6-c9df57dcf48e.png">](https://numpy.org/)
- [<img width="184" src="https://user-images.githubusercontent.com/77333293/206893469-d4f97224-0401-4ad2-b2b3-1498faa25e8b.png">](https://pandas.pydata.org/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

To check out a low-end beta version of this web app, visit: https://colab.research.google.com/drive/1R9tvOwg35IeKIdiRJV9KJlMK0YSKWQRp?usp=sharing

To run the web app locally, you must have Python 3.9.10 locally, then setup your environment following the steps below.

### Prerequisites

Create a new environment for this app to avoid version conflicts:

```
python -m venv </path/to/new/virtual/environment>
```

Activate the new environment:

```
source </path/to/new/virtual/environment>/bin/activate
```

Install all the necessary packages into this virtual environment:

```
pip install -r requirements.txt
```

Fork this repo or download it, then run:

```
python </path/to/project/folder>/main.py
```

### News API

The program includes sending requests to the Newsapi website to obtain recent news article links, if you used mine in the script, it might return no results because I am using a free developer's account that is limited to 200 requests per day. It is recommended that you register your own free Newsapi account and supply it to the web crawling before running it. Here are the steps:

1. Get a free API Key at [https://newsapi.org/](https://newsapi.org/)
2. Enter your API Key on line 77 of the `news_crawl_v2.py` script:
   ```py
   apiKey = 'ENTER YOUR API Key'
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Google Universal Sentence Encoder

The program also uses a pre-trained Google Universal Sentence Encoder model that is 1.04GB on disk and stored in a folder format. Before running the program, you would need to download the zipped folder, and store it under the same directory as the news_to_vector_v2.py file. The one that this GitHub Repo uses is managed by Git LFS, which might not come along with all the other scripts if you forked this repo.

Documentation & downloading for pre-trained Google Universal Sentence Encoder can be found [here](https://tfhub.dev/google/universal-sentence-encoder/4).

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
