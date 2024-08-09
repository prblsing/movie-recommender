# Movie Recommendation System with Vector Databases

This project is a **Research and Development (R&D)** initiative aimed at demonstrating the use of vector databases to build a simple movie recommendation system. The goal is to showcase how vector databases can efficiently manage and search through large, complex datasets by leveraging vector embeddings and similarity searches.

**Important**: This project is not an AI-powered application. Instead, it highlights the capabilities of vector databases in handling high-dimensional data, which is essential for modern data management tasks.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Overview

This project demonstrates how to use vector databases to build a movie recommendation system using the IMDb dataset. By combining movie attributes such as genre, plot, and director into vector embeddings, the system can recommend movies that are semantically similar to a user’s query.

The project uses the following key technologies:
- **Vector Databases**: For storing and querying high-dimensional vector data.
- **FAISS**: Facebook AI Similarity Search, for efficient similarity searches.
- **Streamlit**: For creating an interactive web app to showcase the recommendation system.

## Features

- **Efficient Search**: Leverages vector databases for fast and accurate similarity searches.
- **Streamlit Interface**: Provides a simple and intuitive interface for users to input queries and receive recommendations.
- **R&D Focus**: The project is designed to illustrate the potential of vector databases in modern data management.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:
- **Python 3.7+**
- **Git**
- **Pip** (Python package installer)

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/prblsing/movie-recommender.git
   cd movie-recommender
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download and Prepare the Dataset**:
   - The dataset used in this project is the IMDb movie dataset. You can download it from Kaggle using the following link:
     [IMDb Dataset of Top 1000 Movies and TV Shows](https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows)
   - After downloading, place the `imdb-movie-dataset.csv` file in the project directory.

## Usage

1. **Run the Streamlit App**:
   ```bash
   streamlit run app.py
   ```

2. **Interact with the App**:
   - Open your browser and go to the local URL provided by Streamlit.
   - Enter a movie-related query (e.g., "superhero movie") in the search box.
   - The app will return a list of movies that are semantically similar to your query, based on the vector embeddings.

## Project Structure

```plaintext
movie-recommender/
│
├── app.py                      # Main Streamlit app
├── mov_recommender.py          # Core logic for the recommendation system
├── requirements.txt            # List of dependencies
├── embeddings.pkl              # Precomputed vector embeddings (generated)
├── index.faiss                 # FAISS index for fast searches (generated)
└── README.md                   # Project documentation
```

## Contributing

Contributions are welcome! If you have suggestions for improving the project or adding new features, feel free to fork the repository and submit a pull request.

To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **FAISS**: Facebook AI Similarity Search for efficient vector-based searches.
- **Streamlit**: For providing an easy-to-use framework for deploying data apps.
- **IMDb**: For the dataset used in this project, provided by [Kaggle](https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows).
