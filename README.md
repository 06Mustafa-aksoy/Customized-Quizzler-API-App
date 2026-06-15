# Quizzler - Interactive Quiz Application

A modern, GUI-based quiz application built with Python that fetches random trivia questions and presents them through an interactive interface.

## 🎯 Features

- **Dynamic Question Loading**: Fetches 10 random true/false trivia questions from the Open Trivia Database API
- **Score Tracking**: Keeps track of your score throughout the quiz
- **Visual Feedback**: Displays green for correct answers and red for incorrect answers
- **Interactive GUI**: Built with tkinter for a user-friendly interface
- **HTML Decoding**: Properly decodes HTML entities in questions
- **Error Handling**: Robust error handling for API requests

## 📋 Project Structure

```
Customized-Quizzler-API-App/
├── main.py              # Application entry point
├── question_model.py    # Question class definition
├── quiz_brain.py        # Quiz logic and scoring
├── ui.py                # Graphical user interface
├── data.py              # API integration and data fetching
├── images/              # UI assets (buttons)
│   ├── true.png         # True button image
│   └── false.png        # False button image
└── README.md            # This file
```

## 🏗️ Architecture

The application follows **Object-Oriented Programming (OOP)** principles with clear separation of concerns:

### Classes

1. **`Question`** (`question_model.py`)
   - Represents a single quiz question
   - Stores question text and correct answer
   - Type hints for better code documentation

2. **`QuizBrain`** (`quiz_brain.py`)
   - Manages quiz logic and state
   - Tracks current question number and score
   - Validates user answers
   - Determines quiz completion

3. **`QuizInterface`** (`ui.py`)
   - Creates and manages the GUI
   - Handles button clicks and user interactions
   - Displays questions and feedback
   - Updates score label

4. **`data`** (`data.py`)
   - Fetches questions from Open Trivia Database API
   - Handles API errors gracefully
   - Provides fallback for connection issues

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- `requests` library

### Installation

1. Clone the repository:
```bash
git clone https://github.com/06Mustafa-aksoy/Customized-Quizzler-API-App.git
cd Customized-Quizzler-API-App
```

2. Install required dependencies:
```bash
pip install requests
```

3. Run the application:
```bash
python main.py
```

## 🎮 How to Use

1. Launch the application by running `python main.py`
2. A window will open with the first trivia question
3. Click the **True** button if you think the statement is true
4. Click the **False** button if you think the statement is false
5. Receive instant visual feedback (green = correct, red = incorrect)
6. Your score updates automatically
7. Continue through all 10 questions
8. See your final score at the end

## 📊 API Used

- **[Open Trivia Database](https://opentdb.com/api.php)** - Provides free trivia questions
  - Endpoint: `https://opentdb.com/api.php?amount=10&type=boolean`
  - Returns: 10 random true/false trivia questions with various categories

## ✨ Code Quality Features

- ✅ **Type Hints**: Full type annotations for better code clarity
- ✅ **Docstrings**: Comprehensive documentation for all classes and methods
- ✅ **Error Handling**: Robust error handling for API requests and parsing
- ✅ **Relative Paths**: Uses relative paths for image assets (cross-platform compatible)
- ✅ **Clean Code**: Follows PEP 8 style guidelines

## 🔧 Error Handling

The application handles the following error cases gracefully:

- **Network Timeout**: If the API request times out
- **Connection Error**: If there's no internet connection
- **HTTP Errors**: If the API returns an error status
- **JSON Parsing Errors**: If the API response is malformed

In case of any error, the application displays an error message and uses an empty question list.

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

**Mustafa Aksoy**
- GitHub: [@06Mustafa-aksoy](https://github.com/06Mustafa-aksoy)

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest improvements
- Submit pull requests

## 📞 Support

If you encounter any issues, please open an issue on the GitHub repository.

---

Made with ❤️ by Mustafa Aksoy