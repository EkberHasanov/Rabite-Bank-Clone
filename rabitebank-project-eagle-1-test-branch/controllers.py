from flask import render_template, request
from app import app
from models import Category, News, OnlineTurns, getAllCompanies
from forms import OnlineForm, SearchForm
from xmltodict import parse
from json import loads, dumps
from requests import get
from datetime import date, timedelta


# HOME PAGE
@app.route("/")
def home_page():
    time = date.today() - timedelta(days=1)
    time = time.strftime('%d.%m.%Y')
    url ='https://www.cbar.az/currencies/'
    data = get(url + time + '.xml')
    xpars = parse(data.text)
    str_json = dumps(xpars)
    json_converted = loads(str_json)    
    usd = "{:.4f}".format(float(json_converted['ValCurs']['ValType'][1]['Valute'][0]['Value']))       
    eur = "{:.4f}".format(float(json_converted['ValCurs']['ValType'][1]['Valute'][1]['Value']))
    news_list = News.query.order_by(News.id.desc()).limit(3)
    return render_template("index.html", news_list=news_list, usd_get=usd, eur_get=eur, usd_sales="{:.4f}".format(float(float(usd)*1.001+0.02)), eur_sales="{:.4f}".format(float(float(eur)*1.001+0.02)), news=news, time=time)


# Pass Stuff to Navbar
@app.context_processor
def base():
    form = SearchForm()
    return dict(form=form)


# SEARCH APP
@app.route("/search", methods=["POST"])
def search_result_page():
    form = SearchForm()
    news = News.query
    if form.validate_on_submit():
        # Get data from submited form
        post_searched = form.searched.data
        # Query the Database
        news = news.filter(News.description.like('%' + post_searched + '%'))
        news = news.order_by(News.title).all()
        return render_template("search.html", form=form, searched=post_searched, news=news)
    



# ONLINE TURN PAGE
@app.route("/onlayn-novbe", methods=['GET', 'POST'])
def online_turn():

    post_data = request.form
    print(post_data)
    form = OnlineForm()
    if request.method == "POST":
        form = OnlineForm(data=post_data)
        print(form.filial.data)
        print(form.xidmet.data)
        if form.validate_on_submit():
            contact = OnlineTurns(filial=form.filial.data, xidmet=form.xidmet.data, submit_date=form.date.data, mobile_num=form.mobile_num.data)
            contact.save()
    return render_template("online-form.html", form=form, page='online_turn')


# NEWS PAGE
@app.route("/xeberler")
def news():
    categories = Category.query.all()
    news_list = News.query.all()
    return render_template("news-list.html", news_list=news_list, categories=categories)


# NEWS DETAILS PAGE
@app.route("/xeber/<int:news_id>")
def news_details_page(news_id):
    news_var = News.query.filter_by(id=news_id).first()
    # print(news_var.category_id)
    similar_news_list = News.query.filter_by(category_id=news_var.category_id).limit(3)
    return render_template("news.html", news_var=news_var, similar_news_list=similar_news_list)


# AMANAT PAGE
@app.route("/amanat")
def renderAmanat():
    return render_template('amanat.html', page='amanat')


# AMANAT DETAILS PAGE
@app.route("/amanat-more")
def renderAmanatMore():
    return render_template('amanat-inside.html')

# ORDER PAGE
@app.route("/order")
def renderOrder():
    return render_template('order.html')

# COMPANY PAGE
@app.route("/company")
def renderCompany():
    return render_template('company.html',companies = getAllCompanies(), page='company')

