from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    
    if request.method == 'POST':
        try:
            num1 = float(request.form.get('num1', 0))
            num2 = float(request.form.get('num2', 0))
            
            # Calculate the sum
            sum_result = num1 + num2
            
            # Format the result message
            result = f"The sum of {num1} and {num2} is {sum_result}"
            
        except ValueError:
            result = "Please enter valid numbers"
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(port=1100)
