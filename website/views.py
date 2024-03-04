from flask import Blueprint, render_template, request

views = Blueprint('home','results','about',__name__)

@views.route('/')
def home():
    return render_template("index.html")

@views.route('/results', methods=['GET','POST'])
def results():
    if request.method == 'POST':
        daily_answers = {}
        lifetime_answers = {}
        # Getting the values of div that are named "1answer" used for getting daily score.
        for key, daily_value in request.form.items():
            if key.startswith('1answer'):
                daily_number = key.replace('1answer','')
                daily_answers[daily_number] = daily_value
        total_sum_daily_answers = sum(int(daily_value) for daily_value in daily_answers.values())
        # Getting the values of div that are named "2answer_" use for getting lifetime score.
        for key, lifetime_value in request.form.items():
            if key.startswith('2answer_'):
                lifetime_number = key.replace('2answer','')
                lifetime_answers[lifetime_number] = lifetime_value
        total_sum_lifetime_answers = sum(int(lifetime_value) for lifetime_value in lifetime_answers.values())

        percent_total_daily_answers = (total_sum_daily_answers / 11) * 100

        percent_total_lifetime_answers = (total_sum_lifetime_answers / 36) * 100

        total_perceived = ((total_sum_daily_answers + total_sum_lifetime_answers) / 47) * 100

        lifetime = round(percent_total_lifetime_answers, 2)
        daily = round(percent_total_daily_answers, 2)
        perceived = round(total_perceived, 2)

        if total_perceived <= 30:
            return render_template("results1_30.html", lifetime = lifetime, daily = daily, perceived = perceived)
        elif total_perceived <= 60:
            return render_template("results31_60.html", lifetime = lifetime, daily = daily, perceived = perceived)
        elif total_perceived <= 80:
            return render_template("results61_80.html", lifetime = lifetime, daily = daily, perceived = perceived)
        else:
            return render_template("results81_100.html", lifetime = lifetime, daily = daily, perceived = perceived)

@views.route('/about')
def about():
    return render_template("about.html")

@views.route('/articles')
def articles():
    return render_template("articles.html")