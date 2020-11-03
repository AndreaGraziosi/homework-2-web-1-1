from flask import Flask, request, render_template
import random

app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return"""
    <form action= "/froyo_results" method="GET">
        What is your favorite Fro-Yo flavor> <br/>
        <input type="text" name="flavor"></br>
        What Toppings will you add?</br>
        <label> Enter your Favorite Topping</label>
        <input type="text" name="toppings"></br>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/froyo_results')
def show_froyo_results():
    """Shows the user what they ordered from the previous page."""
    users_froyo_flavor = request.args.get('flavor')
    users_froyo_topping = request.args.get('toppings')
    return f'You ordered {users_froyo_flavor} flavored Fro-Yo and {users_froyo_topping} for your topping!'

@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return  """
   <form action= "/favorite_results" method="GET">
        Please enter the following below:</br>
        <label id="color">Favorite Color</label>
        <input type="text" name="color"></br>
        <label id="animal">Favorite Animal</label>
        <input type="text" name="animal"></br>
        <label id="city">Favorite City</label>
        <input type="text" name="city"></br>
        <input type="submit" value="Submit!">
    </form>
"""

@app.route('/favorite_results')
def favorites_results():
    """Shows the user a nice message using their form results."""
    users_favorite_color = request.args.get('color')
    users_favorite_animal = request.args.get('animal')
    users_favorite_city = request.args.get('city')
    return f'Wow, I didin\'t know {users_favorite_color} {users_favorite_animal}s lived in {users_favorite_city}!'

@app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return """
    <form action="/message_results" method="POST">
         Enter Your Secured Message:
         <input type="text" name="message">
         <input type="submit" value="Submit!">
    </form>
    """

@app.route('/message_results', methods=['POST'])
def message_results():
    
    user_phrase = request.form['message']
    scramble_phrase = sort_letters(user_phrase)
    return f'Here is your Message! {scramble_phrase}'


@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return """
    <form action="/calculator_results" method="GET">
        Please enter 2 numbers and select an operator.<br/><br/>
        <input type="number" name="operand1">
        <select name="operation">
            <option value="add">+</option>
            <option value="subtract">-</option>
            <option value="multiply">*</option>
            <option value="divide">/</option>
        </select>
        <input type="number" name="operand2">
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/calculator_results')
def calculator_results():
    """Shows the user the result of their calculation."""
    first_number = request.args.get('operand1')
    math_operation = request.args.get('operation')
    second_number = request.args.get('operand2')
    result = request.args.get('operand1') request.args.get('operation') request.args.get('operand2')
    if math_operation== 
    
    return f'if you choose to {} {first_number} and {second_number} Your result will be: {result}'

# List of compliments to be used in the `compliments_results` route (feel free 
# to add your own!) 
# https://systemagicmotives.com/positive-adjectives.htm
list_of_compliments = [
    'awesome',
    'beatific',
    'blithesome',
    'conscientious',
    'coruscant',
    'erudite',
    'exquisite',
    'fabulous',
    'fantastic',
    'gorgeous',
    'indubitable',
    'ineffable',
    'magnificent',
    'outstanding',
    'propitioius',
    'remarkable',
    'spectacular',
    'splendiferous',
    'stupendous',
    'super',
    'upbeat',
    'wondrous',
    'zoetic'
]

@app.route('/compliments')
def compliments():
    """Shows the user a form to get compliments."""
    return render_template('compliments_form.html')

@app.route('/compliments_results')
def compliments_results():
    """Show the user some compliments."""
    context = {
        # TODO: Enter your context variables here.
    }

    return render_template('compliments_results.html', **context)


if __name__ == '__main__':
    app.run()
