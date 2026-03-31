# 🧠 AI Sentiment Analyzer

> A simple, beginner-friendly machine learning tool that reads a sentence and tells you whether it's **positive** or **negative** — powered by Python and scikit-learn.

---

## 💡 What Does This Do?

Ever wondered if a piece of text sounds happy, angry, or somewhere in between? That's exactly what this tool figures out.

You type in any sentence — like *"I love this movie!"* or *"Today was a terrible day"* — and the analyzer uses a trained machine learning model to instantly tell you the **sentiment** behind it.

It also keeps a **history** of everything you've analyzed, so you can look back at past results anytime.

---

## 📁 What's Inside the Project?

```
sentiment_analyzer/
├── sentiment_analyzer.py   # The main Python script — this is where all the magic happens
├── ds.csv                  # Training dataset with labeled phrases (positive/negative)
├── model.pkl               # The pre-trained ML model (auto-generated if missing)
└── history.csv             # Your personal analysis history (grows as you use the tool)
```

---

## 🚀 Getting Started

### 1. Make Sure You Have the Requirements

You'll need Python 3 installed, along with these libraries:

```bash
pip install pandas scikit-learn
```

### 2. Run the Tool

Navigate to the project folder and run:

```bash
python sentiment_analyzer.py
```

That's it! The program will start up and show you a simple menu.

---

## 🖥️ How to Use It

Once you run the script, you'll see a menu like this:

```
1. Enter Text
2. About
3. Help
4. View History
0. Exit
```

Here's what each option does:

| Option | What It Does |
|--------|-------------|
| **1. Enter Text** | Type any sentence and get an instant sentiment result |
| **2. About** | Shows a short description of the tool |
| **3. Help** | Displays the menu options again |
| **4. View History** | Shows the last 5 sentences you analyzed |
| **0. Exit** | Closes the program |

### Example Interaction

```
choice: 1
enter: Japan is a great country
result: positive
```

Simple, clean, and to the point!

---

## 🤖 How Does It Work (The Non-Geeky Version)?

1. **Training Data** — The tool learns from `ds.csv`, a dataset full of example phrases already labeled as "positive" or "negative".

2. **Vectorization** — It converts text into numbers using a technique called **TF-IDF** (don't worry about the name — it just means it figures out which words matter most).

3. **Logistic Regression** — A classic and reliable ML algorithm analyzes those numbers and makes a prediction.

4. **Model Saving** — Once trained, the model is saved to `model.pkl` so you don't have to wait for retraining every time you open the tool.

5. **History Logging** — Every prediction is quietly saved to `history.csv` so you can review past results.

---

## 📊 About the Dataset

The training dataset (`ds.csv`) contains a collection of labeled phrases. Each row looks like this:

| phrase | sentiment |
|--------|-----------|
| "I love spending time with my family." | positive |
| "Sunshine always brightens my day." | positive |
| *(and many more...)* | ... |

The model learns patterns from these examples and applies them to whatever new text you throw at it.

---

## 🔄 What Happens If the Model File Is Missing?

No problem! If `model.pkl` doesn't exist when you launch the tool, it will **automatically retrain** itself from `ds.csv` and save a fresh model. You just need to make sure `ds.csv` is present.

---

## ⚠️ A Few Things to Keep in Mind

- **Input can't be empty** — If you press Enter without typing anything, the tool will remind you to enter some text.
- **Case doesn't matter** — The model handles lowercase conversion internally, so you can type however you like.
- **History shows last 5 entries** — The View History option only displays your 5 most recent results to keep things clean.
- **Encoding handled automatically** — The tool tries UTF-8 first and falls back to Latin-1 if needed, so most datasets should load without issues.

---

## 🛠️ For Developers: Quick Code Overview

The script is organized into clean, single-purpose functions:

| Function | What It Does |
|----------|-------------|
| `loaddata()` | Reads and validates the CSV dataset |
| `trainmodel(df)` | Trains the TF-IDF + Logistic Regression model |
| `loadmodel()` | Loads existing model or triggers training if absent |
| `predict(data, txt)` | Runs a sentiment prediction on input text |
| `savehist(txt, res)` | Appends a result to the history CSV |
| `showhist()` | Displays the last 5 history entries |
| `main()` | Runs the interactive menu loop |

---

## 🌱 Ideas for Future Improvements

Want to take this project further? Here are some fun directions:

- Add a **"neutral"** sentiment category for mixed feelings
- Build a simple **web interface** using Flask or Streamlit
- Support **batch analysis** — analyze a whole CSV file at once
- Add **confidence scores** to show how sure the model is
- Improve accuracy by training on a larger or domain-specific dataset

---

## 📝 License

This project is open for learning and personal use. Feel free to modify, extend, and experiment with it!

---

*Built with Python 🐍 | scikit-learn 🤖 | pandas 🐼*
