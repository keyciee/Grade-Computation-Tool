from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculationsnya(): 
    result_message = '' 
    if request.method =='POST':
        preliminary = request.form.get('preliminary')
        
        try:
            preliminary = float(preliminary) if preliminary else None 
            
            totalgradenya = 75

            if preliminary is not None and (preliminary < 0 or preliminary > 20): 
                result_message = "Invalid input. Preliminary grade must be between 0 and 20."
            elif preliminary is not None:
                midterm_requirementnya = (totalgradenya - preliminary * 0.20) * (0.30 / (0.30 + 0.50))
                final_requirementnya = (totalgradenya - preliminary) - midterm_requirementnya
                result_message = (
                    f"In order to pass with a Prelim grade of {preliminary:.2f}, you need:<br>" \
                    f"- Midterm Grade: {midterm_requirementnya:.2f} or higher<br>" \
                    f"- Final Grade: {final_requirementnya:.2f} or higher."
                )
            
        except ValueError:
            result_message = "Invalid Input! Please enter valid numeric value for Preliminary grade."

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Grade Computation Tool</title>
        <style>
            body {{
                margin: 0;
                padding: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(to bottom, silver, white);
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                color: #333;
            }}

            .container {{
                background: #ffffff;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                padding: 30px;
                width: 400px;
                text-align: center;
                max-width: 90%;
            }}

            h1 {{
                color: #333;
                font-size: 28px;
                margin-bottom: 20px;
            }}

            input[type="text"], input[type="submit"] {{
                width: 100%;
                padding: 12px;
                margin: 10px 0;
                border-radius: 5px;
                border: 1px solid #ccc;
                font-size: 16px;
                box-sizing: border-box;
                outline: none;
            }}

            input[type="text"] {{
                background-color: #fafafa;
            }}

            input[type="text"]:focus {{
                border-color: #66b3ff;
                background-color: #ffffff;
            }}

            input[type="submit"] {{
                background-color: green;
                color: white;
                border: none;
                cursor: pointer;
                font-size: 18px;
                transition: background-color 0.3s ease;
            }}

            input[type="submit"]:hover {{
                background-color: darkgreen;
            }}

            .result {{
                margin-top: 20px;
                font-size: 18px;
                color: #333;
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 5px;
                background-color: #f9f9f9;
            }}

        </style>
    </head>
    <body>
        <div class="container">
            <h1>Grade Computation Tool</h1>
            <form method="post">
                <input type="text" name="preliminary" placeholder="Enter Prelim Grade (0-20)">
                <input type="submit" value="Compute">
            </form>
            <div class="instruction">
                Grade Composition: <br>
                Prelim Grade: 20%<br>
                Midterm Grade: 30%<br>
                Final Grade: 50%<br>
                Total Passing Grade: 75%<br>
            </div>
            <div class="result">{result_message}</div>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)