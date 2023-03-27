

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myproject.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.app_context().push()
db = SQLAlchemy(app)


class books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bookid = db.Column(db.String(50), nullable=False, unique=True)
    title = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    publisher = db.Column(db.String(50), nullable=False)
    published_year = db.Column(db.Date, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    status=db.Column(db.String(20),nullable=False)

    def __repr__(self):
        return f"{self.bookid},{self.title},{self.author},{self.publisher},{self.published_year},{self.price},{self.id}"


class students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usn = db.Column(db.String(50), nullable=False, unique=True)
    name = db.Column(db.String(50), nullable=False)
    semester = db.Column(db.String(10), nullable=False)
    dept = db.Column(db.String(50), nullable=False)
    mobno = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"{self.id},{self.usn},{self.name}"
  
class reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usn = db.Column(db.String(50),ForeignKey(students.usn), nullable=False,)
    bookid = db.Column(db.String(50),ForeignKey(books.bookid),nullable=False)
    rdate= db.Column(db.Date, nullable=False)
    status = db.Column(db.String(50), nullable=False)
       
    def __repr__(self):
        return f"{self.id},{self.usn},{self.bookid},{self.rdate},{self.status}"


@app.route('/cancelreservation/<bookid>,<rid>')
def cancelreservation(bookid,rid):
    
    #msg=f'recevid parameters are bookid = {bookid},reservation id {rid}'
    
    book=books.query.filter_by(bookid=bookid).first()
    book.status='available'
    db.session.commit()
    
    reser=reservation.query.get(rid)
    db.session.delete(reser)
    db.session.commit()