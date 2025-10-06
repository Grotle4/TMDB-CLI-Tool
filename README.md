# 🎬 Movie Info CLI

A simple Python command-line tool that retrieves and displays categorized movie information from **The Movie Database (TMDB)** API.  
The app fetches data such as **Now Playing**, **Popular**, **Top Rated**, and **Upcoming** movies, along with their **titles** and **descriptions**.
Part of project for Roadmap.sh: https://roadmap.sh/projects/tmdb-cli

---

## 🧭 Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Examples](#examples)
- [Error Handling](#error-handling)
- [Dependencies](#dependencies)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## 📖 Introduction

This CLI tool interacts with the TMDB API to fetch movie information categorized by type (e.g., “popular”, “top rated”, etc.).  
Each movie result displays its **title** and **overview (description)** for a more informative terminal output.

---

## ✨ Features

- Retrieve categorized movie data:
  - 🎥 Now Playing
  - 🌟 Popular
  - 🏆 Top Rated
  - 🚀 Upcoming
- Secure API key management using `.env`
- Prints movie **titles** and **descriptions**
- Includes robust error handling for API and connection issues

---

## ⚙️ Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/movie-info-cli.git
   cd movie-info-cli
   ```

2. **(Optional) Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate    # macOS/Linux
   venv\Scripts\activate       # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file** in the project root and add your TMDB API key:
   ```bash
   API_KEY=your_tmdb_api_key_here
   ```

---

## 🔧 Configuration

- Get a free API key from [The Movie Database (TMDB)](https://developer.themoviedb.org/reference/intro/getting-started).
- Store your key securely in the `.env` file as shown above.
- The script automatically loads the key via the `dotenv` package.

---

## 🚀 Usage

Run the script from the command line with the `-t` or `--type` argument:

```bash
python main.py -t <movie_type>
```

**Available options:**
- `playing` → Movies now playing  
- `popular` → Popular movies  
- `top` → Top-rated movies  
- `upcoming` → Upcoming movie releases  

---

## 💡 Examples

```bash
# Fetch now playing movies
python main.py -t playing

# Fetch popular movies
python main.py -t popular

# Fetch top rated movies
python main.py -t top

# Fetch upcoming releases
python main.py -t upcoming
```

---

## ⚠️ Error Handling

The app gracefully handles:
- `HTTPError` → Invalid responses from TMDB API  
- `ConnectionError` → Network issues  
- `Timeout` → Request timeout  
- `RequestException` → Any unknown request error  

---

## 📦 Dependencies

- `requests`
- `python-dotenv`
- `argparse` *(standard library)*
- `os` *(standard library)*

Install all with:
```bash
pip install requests python-dotenv
```

---

## 🧰 Troubleshooting

| Issue | Possible Cause | Solution |
|-------|----------------|-----------|
| `API_KEY is None` | Missing `.env` file or invalid key | Verify `.env` exists and contains `API_KEY=your_key` |
| `401 Unauthorized` | Invalid or expired TMDB key | Regenerate your API key |
| `ConnectionError` | Network issue | Check internet connection and retry |
| `Timeout` | Slow response from TMDB | Retry later |

---

## 🪪 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.
