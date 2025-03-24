# Higher Lower Instagram Followers Game
A command-line game that challenges players to guess which Instagram user has more followers.

## 📝 Description

The Higher Lower Instagram Game is a simple yet addictive command-line game where players compare two Instagram users and guess which one has more followers. The game continues until the player makes an incorrect guess, with the score increasing for each correct answer.

## ✨ Features

- Random selection of Instagram users from a predefined dictionary
- Displays user profession and country for each comparison
- Simple A/B selection mechanic
- Running score tracking
- Clean and engaging ASCII art interface

## 🎮 How to Play

1. The game presents two Instagram users (A and B) with their profession and country
2. Look at both users and guess which one has more followers
3. Type 'A' or 'B' to make your selection
4. If correct, your score increases by 1 and you continue to the next round
5. If incorrect, the game ends and displays your final score

## 🛠️ Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/higher-lower-instagram-game.git
   cd higher-lower-instagram-game
   ```

2. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```

## 🚀 Usage

Run the game with:
```
python higher_lower_game.py
```

## 📂 Project Structure

```
higher-lower-instagram-game/
├── higher_lower_game.py    # Main game file
├── art.py                  # Contains ASCII art (LOGO and VS)
├── word_dictionary.py      # Dictionary of Instagram users with their data
├── requirements.txt        # Required packages
└── README.md               # This file
```

## 🧩 Files Description

- **higher_lower_game.py**: Contains the main game logic
- **art.py**: Contains ASCII art for the game logo and "VS" display
- **word_dictionary.py**: Contains the INSTAGRAM_USERS_DICTIONARY with user data including:
  - Profession
  - Country
  - Follower count

## 🔄 Game Logic

1. Randomly select an Instagram user A
2. Randomly select a different Instagram user B
3. Display both users with their information
4. Prompt player for a guess
5. Compare follower counts and determine if player is correct
6. If correct, user B becomes user A in the next round and a new user B is selected
7. If incorrect, end the game and display final score

## 🔮 Future Enhancements

- High score tracking using a text file
- Additional user statistics
- Difficulty levels
- Time-based challenges
- Graphical user interface

## 📋 Requirements

- Python 3.6 or higher
- 
## 📝 License
This project is open source and available under the [MIT License](LICENSE)..
