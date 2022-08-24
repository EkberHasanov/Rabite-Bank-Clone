from extensions import db
from sqlalchemy import func


class Category(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(20), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Companies(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100),nullable = False)
    img_url = db.Column(db.Text,nullable = False)
    
    def __init__(self,name,img_url):
        self.name = name 
        self.img_url = img_url        

    def save(self):
        db.session.add(self)
        db.session.commit()


class News(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    share_date = db.Column(db.DateTime(timezone=True), default=func.now())
    # Foreign Key To Link Categories
    category_id = db.Column(db.Integer(), db.ForeignKey('category.id'))
    category = db.relationship('Category', backref=db.backref('categories', lazy='dynamic'))

    def __init__(self, title, image, description, share_date, category_id):
        self.title = title
        self.image = image
        self.description = description
        self.share_date = share_date
        self.category_id = category_id
    
    def __repr__(self):
        return self.title

    def save(self):
        db.session.add(self)
        db.session.commit()

class OnlineTurns(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    filial = db.Column(db.String(255))
    xidmet = db.Column(db.String(255))
    submit_date = db.Column(db.String(255))
    mobile_num = db.Column(db.String(255))

    def __init__(self, filial, xidmet, submit_date, mobile_num):
        self.filial = filial
        self.xidmet = xidmet
        self.submit_date = submit_date
        self.mobile_num = mobile_num
    
    
    def save(self):
        db.session.add(self)
        db.session.commit()
def getAllCompanies():
    comps = Companies.query.all()
    return comps


class CardOrder(db.Model):
    id = db.Column(db.Integer(), primary_key = True)


comp1 = Companies("Faizsiz Avans","https://www.rabitabank.com/uploads/posts/2021/10/esas.png")
comp1.save()

comp1 = Companies("Lombard krediti üzrə Kampaniya","https://www.rabitabank.com/uploads/posts/2022/02/lombard%20kampaniya.png")
comp1.save()

comp1 = Companies("Nağd pul krediti üzrə kampaniya","https://www.rabitabank.com/uploads/posts/2022/04/bannerrrr.png")
comp1.save()
