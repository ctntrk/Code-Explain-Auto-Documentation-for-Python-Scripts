import ast
import gradio as gr

class CodeDocGenerator(ast.NodeVisitor):
    def __init__(self):
        self.docs = []
        self.indent_level = 0

    def indent(self):
        return "  " * self.indent_level

    def visit_Module(self, node):
        self.docs.append("# 📘 Code Analysis and Auto Documentation\n")
        self.generic_visit(node)

    def visit_Import(self, node):
        names = ", ".join([alias.name for alias in node.names])
        self.docs.append(f"- 📦 Import: `{names}`")

    def visit_ImportFrom(self, node):
        module = node.module or ""
        names = ", ".join([alias.name for alias in node.names])
        self.docs.append(f"- 📦 From `{module}` import `{names}`")

    def visit_ClassDef(self, node):
        prefix = self.indent()
        docstring = ast.get_docstring(node) or "No class docstring found."
        self.docs.append(f"{prefix}## 🧱 Class: `{node.name}` (Line {node.lineno})")
        self.docs.append(f"{prefix}- 📄 Docstring: {docstring}")
        self.indent_level += 1
        self.visit_body_elements(node.body)
        self.indent_level -= 1

    def visit_FunctionDef(self, node):
        prefix = self.indent()
        args = [arg.arg for arg in node.args.args]
        docstring = ast.get_docstring(node) or "No function docstring found."
        self.docs.append(f"{prefix}### 🔧 Function: `{node.name}` (Line {node.lineno})")
        self.docs.append(f"{prefix}- 🧩 Arguments: {', '.join(args) if args else 'None'}")
        self.docs.append(f"{prefix}- 📄 Docstring: {docstring}")
        self.indent_level += 1
        self.visit_body_elements(node.body)
        self.indent_level -= 1

    def visit_Assign(self, node):
        prefix = self.indent()
        targets = ", ".join(ast.unparse(t) if hasattr(ast, "unparse") else "?" for t in node.targets)
        value = ast.unparse(node.value) if hasattr(ast, "unparse") else "?"
        self.docs.append(f"{prefix}- 📝 Assignment: `{targets} = {value}`")

    def visit_For(self, node):
        prefix = self.indent()
        target = ast.unparse(node.target) if hasattr(ast, "unparse") else "?"
        iter_ = ast.unparse(node.iter) if hasattr(ast, "unparse") else "?"
        self.docs.append(f"{prefix}- 🔁 For loop: `for {target} in {iter_}`")
        self.indent_level += 1
        self.visit_body_elements(node.body)
        self.indent_level -= 1

    def visit_Call(self, node):
        prefix = self.indent()
        func_name = ""
        if isinstance(node.func, ast.Attribute):
            func_name = f"{ast.unparse(node.func.value) if hasattr(ast, 'unparse') else '?'}.{node.func.attr}"
        elif isinstance(node.func, ast.Name):
            func_name = node.func.id
        self.docs.append(f"{prefix}- 📞 Function call: `{func_name}`")
        self.generic_visit(node)

    def visit_Return(self, node):
        prefix = self.indent()
        value = ast.unparse(node.value) if (node.value and hasattr(ast, "unparse")) else "?"
        self.docs.append(f"{prefix}- 🔙 Return statement: `{value}`")

    def visit_body_elements(self, body):
        for elem in body:
            self.visit(elem)


def analyze_code(file):
    if file is None:
        return (
            "### ⚠️ No file uploaded! **Please upload a `.py` file to generate documentation.** ⚠️",
            ""
        )
    try:
        source_code = file.read().decode("utf-8") if hasattr(file, "read") else open(file, "r", encoding="utf-8").read()
        tree = ast.parse(source_code)
        doc_gen = CodeDocGenerator()
        doc_gen.visit(tree)
        return "\n".join(doc_gen.docs), source_code
    except Exception as e:
        return f"❌ Error: {str(e)}", ""

def clear_all():
    return None, "", ""

info_text = """
### 📘 General Information

This tool automatically analyzes uploaded Python source files (`.py`) and generates easy-to-read documentation.  
It uses Python's **Abstract Syntax Tree (AST)** 🧬 to identify key code elements such as:

- 📦 **Imports**
- 🧱 **Classes**
- 🔧 **Functions**
- 📝 **Assignments**
- 🔁 **Loops**
- 📞 **Function Calls**
- 🔙 **Return Statements**

All extracted details are displayed in Markdown 🗒️ format for better readability and portability.

---

### 🚀 How to Use

1. 📂 **Upload** a Python file (`.py`) using the panel on the **left**.  
2. 🧠 The tool **automatically analyzes** the file and shows:
   - 📄 The original **source code**
   - 🧾 The **generated documentation**
3. 🧹 Click **Clear All** to reset and upload another file.

---

### 🛠️ Technologies Used

- 🐍 **Python** — Main programming language  
- 🧬 **AST (Abstract Syntax Tree)** — For parsing Python code structure  
- 🧰 **Gradio** — Web-based interactive UI framework  
- 🗒️ **Markdown** — For formatting and presenting the output documentation  

---

### 🤝 Who Is This For?

This tool is perfect for:

- 👩‍💻 Developers who want quick insight into unfamiliar code  
- 📚 Students learning Python structure  
- 📋 Teams documenting legacy Python projects

"""



with gr.Blocks(title="CodeExplain", theme=gr.themes.Base()) as iface:
    with gr.Accordion("ℹ️ About / Info", open=False):
        gr.Markdown(info_text)

    with gr.Row():
        with gr.Column(scale=1):
            file_input = gr.File(
                file_types=[".py"],
                label="📂 Upload a Python File (.py)",
                interactive=True
            )
            clear_btn = gr.Button("🧹 Clear All")

            doc_output = gr.Markdown(label="🧾 Auto-Generated Documentation")

        with gr.Column(scale=1):
            code_output = gr.Code(label="📄 Source Code", language="python")

    file_input.change(fn=analyze_code, inputs=file_input, outputs=[doc_output, code_output])
    clear_btn.click(fn=clear_all, inputs=None, outputs=[file_input, doc_output, code_output])

if __name__ == "__main__":
    iface.launch()