from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine 
from database import Session 
from database import record 
from datetime import datetime

app = Flask(__name__)
def calculate_tdee(weight, height, age, gender, activity_level):
        weight = float(weight)
        height = float(height)
        age = float(age)
        activity_level = float(activity_level)
        if gender == 'male':
            bmr = 10 * weight + 6.25 * height - 5 * age + 5
        elif gender == 'female':
            bmr = 10 * weight + 6.25 * height - 5 * age - 161
        else:
            return 'Invalid gender'
        tdee = bmr*activity_level
        return tdee

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tdeecalculator.html', methods=['GET', 'POST'])
def track_calorie():
    if request.method == 'POST':
        weight = request.form.get('weight')
        height = request.form.get('height')
        age = request.form.get('age')
        gender = request.form.get('gender')
        activity_level = request.form.get('activity_level')
        tdee = calculate_tdee(weight, height, age, gender, activity_level)
        return 'Your TDEE is: ' + str(tdee)
    return render_template('tdeecalculator.html')

@app.route('/mealplanner.html')
def meal_planner():
    if request.method == 'POST':
        food = request.form.get('food')
        calories = request.form.get('calories')
    UPDATE = record.insert().values(food = food, calories = calories)
    return render_template('mealplanner.html')

session = Session()

if __name__ == "__main__":
    app.run(debug=True)




