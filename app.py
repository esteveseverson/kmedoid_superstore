from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

medoid_918 = [80134.40, 40, 2, 5, 3, 6, 6, 1]
medoid_1064 = [52157.22, 40, 2, 3, 2, 5, 4, 0]
min_max_values = [
    (1730.0, 666666.0),
    (0.0, 99.0),
    (0.0, 15.0),
    (0.0, 27.0),
    (0.0, 28.0),
    (0.0, 13.0),
    (0.0, 20.0),
    (0.0, 1.0),
]

def normalize(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val)

@app.route('/')
def index():
    return render_template('index.html', title='Medoid Finder')

@app.route('/form')
def form():
    return render_template('form.html', title='Medoid Finder')

@app.route('/about')
def about():
    return render_template('about.html', title='Sobre o Medoid Finder')

@app.route('/dataset')
def dataset():
    return render_template('dataset.html', title='Sobre a base de dados')

@app.route('/result', methods=['POST'])
def result():
    income = float(request.form['income'])
    recency = float(request.form['recency'])
    num_deals_purchases = float(request.form['num_deals_purchases'])
    num_web_purchases = float(request.form['num_web_purchases'])
    num_catalog_purchases = float(request.form['num_catalog_purchases'])
    num_store_purchases = float(request.form['num_store_purchases'])
    num_web_visits_month = float(request.form['num_web_visits_month'])
    response = float(request.form['response'])

    new_entry = [
        income, recency, num_deals_purchases, num_web_purchases, num_catalog_purchases,
        num_store_purchases, num_web_visits_month, response
    ]

    norm_medoid_918 = [normalize(medoid_918[i], min_max_values[i][0], min_max_values[i][1]) for i in range(len(medoid_918))]
    norm_medoid_1064 = [normalize(medoid_1064[i], min_max_values[i][0], min_max_values[i][1]) for i in range(len(medoid_1064))]
    norm_new_entry = [normalize(new_entry[i], min_max_values[i][0], min_max_values[i][1]) for i in range(len(new_entry))]

    dist_to_918 = sum([(norm_new_entry[i] - norm_medoid_918[i]) ** 2 for i in range(len(norm_new_entry))]) ** 0.5
    dist_to_1064 = sum([(norm_new_entry[i] - norm_medoid_1064[i]) ** 2 for i in range(len(norm_new_entry))]) ** 0.5

    closest_medoid = 918 if dist_to_918 < dist_to_1064 else 1064

    return render_template('result.html', title='Resultado', medoid=closest_medoid)

if __name__ == '__main__':
    app.run(debug=True)
