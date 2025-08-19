# 📘 CodeExplain: Auto Documentation for Python Scripts

**Upload your Python scripts and get instant, clear, Markdown-formatted documentation generated automatically!**

CodeExplain leverages Python’s Abstract Syntax Tree (AST) to analyze your `.py` files and produce human-friendly, structured documentation covering imports, classes, functions, assignments, loops, function calls, and return statements.

---

## 🌐 Live Demo

Try it instantly here:  
🔗 [CodeExplain Demo](https://huggingface.co/spaces/ctntrk/CodeExplain)

---

## 🚀 Features

* 🐍 Upload and analyze Python `.py` files automatically  
* 🧬 AST-powered extraction of code structure and elements  
* 🧱 Auto-document classes, methods, and functions with docstrings  
* 📝 Show variable assignments, loops, function calls, and return statements  
* 🗒️ Generates neat Markdown output for easy reading and sharing  
* 🧹 Clear/reset button to analyze new files quickly  
* 💻 User-friendly web interface built with Gradio  

---

## 🧠 Technologies Used

* **Python** — core programming language  
* **AST (Abstract Syntax Tree)** — parsing Python code structure  
* **Gradio** — interactive web UI framework  
* **Markdown** — formatting generated documentation  

---

## 🚀 How It Works

1. **File Upload:** Upload a `.py` file via the interface.  
2. **AST Parsing:** The backend parses your code using Python’s AST module.  
3. **Code Analysis:** Extracts imports, classes, functions, assignments, loops, calls, and return statements.  
4. **Docstring Extraction:** Retrieves and includes docstrings for classes and functions if present.  
5. **Documentation Generation:** Formats the extracted data into clean Markdown.  
6. **Display:** Shows the original source code alongside the generated documentation.  

---

## 👥 Who Can Use This?

* 👩‍💻 Developers needing quick insights into unfamiliar Python code  
* 📚 Students learning Python and code structure  
* 📋 Teams documenting legacy Python projects  
* 📝 Anyone looking to generate readable Python code documentation fast  

---

## 🔧 Getting Started

To run the project locally:

### 1. Install dependencies:

```bash
pip install gradio
````

### 2. Run the app:

```bash
python app.py
```

> The app launches a local web interface where you can upload `.py` files and get documentation instantly.

---

## 📄 License

This project is released under the **Apache 2.0 License**.

---

## 📬 Feedback & Contributions

Contributions, suggestions, and bug reports are welcome! Feel free to open issues or pull requests.

 
