# PinSuggest

PinSuggest is a web scraping application designed to fetch images and their respective links from the Pinterest ideas section. Whether you're seeking inspiration or looking for specific themed images, PinSuggest simplifies the process by retrieving and organizing images based on topics. This project aims to assist users in navigating the vast selection of images available on Pinterest and provides features for favoriting and managing images for easy access later.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
  - [CLI Usage](#cli-usage)
- [Built With](#built-with)
- [Features](#features)
- [Motivation](#motivation)
- [Contributing](#contributing)
- [License](#license)


## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
  - [CLI Usage](#cli-usage)
- [Built With](#built-with)
- [Features](#features)
- [Motivation](#motivation)
- [Contributing](#contributing)
- [License](#license)

## Installation
1. **Clone the repository:**
    ```bash
    git clone https://github.com/thigazzz/pin-suggest.git
    cd pin-suggest
    ```

2. **Install packages:**
    ```bash
    virtualenv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

3. **Set up the project environment:**
    ```bash
    python3 setup.py
    ```

## Usage
### CLI Usage

Run the CLI script:
```bash
python3 cli.py
```

There are 5 commands available: show_topics, images, favorite, unfavorite, and favorited.
```
show_topics: Show available topics to get images.
>>> show_topics
```
```
images: Show images of a chosen topic.
>>> images [number of topic] [number of images to get]
```
```
favorite: Favorite and save an image to the database.
>>> favorite [number of image]
```
```
unfavorite: Unfavorite and remove an image from the database.
>>> unfavorite [number of image]
```
```
favorited: Show all favorited images.
>>> favorited
```


## Built With
- [Requests (Webscrap)](https://pypi.org/project/requests/)
- [BeatifulSoup4 (Webscrap)](https://pypi.org/project/beautifulsoup4/)
- [Class CLI (CLI)](https://pypi.org/project/class-cli/)
- [Caribou (Migrations)](https://github.com/clutchski/caribou)

## Features
- [x] **Topic-Based Image Retrieval**: Provide images from a specific topic on Pinterest.
- [x] **Diverse Image Selection**: Ensure that the images provided are different from each other.
- [x] **Customizable Image Count**: Allow users to set the number of images to be retrieved (default is 10).
- [x] **Image Favoriting**: Enable users to favorite an image and store its link for later reference.
- [x] **Favorites Management**: Provide CRUD (Create, Read, Update, Delete) operations for managing favorited images.

## Motivation
The motivation behind PinSuggest is twofold. Firstly, it aims to assist individuals who, like me, struggle to choose an image from a vast selection available on Pinterest. This can be particularly overwhelming when searching for inspiration or specific themes. Secondly, this project serves as a platform for me to enhance my technical skills, particularly in Python programming, web scraping, and Robotic Process Automation (RPA). By tackling a real-world problem and implementing a practical solution, I hope to refine my abilities in designing, developing, and testing applications.

## Contributing
We welcome contributions from the community! If you'd like to contribute to PinSuggest, please follow these steps:

    Fork the repository.
    Create a new branch for your feature or bugfix (git checkout -b feature/your-feature).
    Make your changes and commit them (git commit -m 'Add some feature').
    Push your changes to your branch (git push origin feature/your-feature).
    Open a pull request describing your changes.

Please ensure your code follows the project's coding standards and includes tests where applicable. We appreciate your contributions!

## License
This project is licensed under the MIT License - see the LICENSE file for details.
