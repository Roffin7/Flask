from flask import Flask,request,render_template,jsonify

app=Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/math',methods=['POST'])
def math_ops1():
    if request.method == 'POST':
        ops=request.form['operation']
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        
        if ops == 'add':
            result=f"The sum of {num1} and {num2} : {num1+num2}"
        if ops == 'subtract':
            result=f"The subtract of {num1} and {num2} : {num1-num2}"        
        if ops == 'multiply':
            result=f"The multiply of {num1} and {num2} : {num1*num2}"
        if ops == 'divide':
            try:
                result=f"The divide of {num1} and {num2} : {num1/num2}"
            except:
                result=f"Zero Division error,if num2=0"
    return render_template('results.html',result=result)

# Check Using Postman
@app.route('/json',methods=['POST'])
def math_ops():
    if request.method == 'POST':
        ops=request.json['operation']
        num1=int(request.json['num1'])
        num2=int(request.json['num2'])
        
        if ops == 'add':
            result=f"The sum of {num1} and {num2} : {num1+num2}"
        if ops == 'subtract':
            result=f"The subtract of {num1} and {num2} : {num1-num2}"        
        if ops == 'multiply':
            result=f"The multiply of {num1} and {num2} : {num1*num2}"
        if ops == 'divide':
            try:
                result=f"The divide of {num1} and {num2} : {num1/num2}"
            except:
                result=f'Zero Division error,if num2=0'
    return jsonify(result)
    
    
if __name__ == "__main__":
    app.run(host="0.0.0.0")
                