from flask import Flask, render_template_string, request, redirect, url_for
import os

app = Flask(__name__)

# In-memory storage for shopping list
shopping_list = []

# HTML template (embedded in app.py for simplicity)
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Shopping List App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f0f0f0;
        }
        .container {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #333;
            text-align: center;
        }
        form {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
        }
        input[type="text"] {
            flex: 1;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        button {
            padding: 8px 16px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 8px;
            border-bottom: 1px solid #ddd;
        }
        .delete-btn {
            background-color: #f44336;
        }
        .delete-btn:hover {
            background-color: #da190b;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Shopping List</h1>
        <form action="/add" method="post">
            <input type="text" name="item" placeholder="Enter item" required>
            <button type="submit">Add Item</button>
        </form>
        
        <ul>
            {% for item in items %}
            <li>
                {{ item }}
                <form action="/delete" method="post" style="margin: 0;">
                    <input type="hidden" name="item" value="{{ item }}">
                    <button type="submit" class="delete-btn">Delete</button>
                </form>
            </li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, items=shopping_list)

@app.route('/add', methods=['POST'])
def add_item():
    item = request.form.get('item')
    if item and item not in shopping_list:
        shopping_list.append(item)
    return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete_item():
    item = request.form.get('item')
    if item in shopping_list:
        shopping_list.remove(item)
    return redirect(url_for('index'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)