from flask_script import Manager
from project import app, db, Movie, Actor

manager = Manager(app)


@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    movie1 = Movie(title= 'Just Go With It', year=2011, genre='Comedy/Romance', description='Plot: His heart recently broken, plastic surgeon Danny Maccabee (Adam Sandler) pretends to be married so he can enjoy future dates with no strings attached. ')
    movie2 = Movie(title= 'Maleficent', year=2014, genre='Fantasy', description='Plot: As a beautiful young woman of pure heart, Maleficent (Angelina Jolie) has an idyllic life in a forest kingdom. When an invading army threatens the land, Maleficent rises up to become its fiercest protector.')
    movie3 = Movie(title= 'Mr. & Mrs. Smith', year=2005, genre='Action', description='Plot: John (Brad Pitt) and Jane Smith (Angelina Jolie), a couple in a stagnating marriage, live a deceptively mundane existence. However, each has been hiding a secret from the other: they are assassins working for adversarial agencies.')
    movie4 = Movie(title= 'Grown Ups', year=2010, genre='Comedy', description='Plot: The death of their childhood basketball coach leads to a reunion for some old friends (Adam Sandler, Kevin James, Chris Rock), who gather at the site of a championship celebration years earlier. Picking up where they left off, the buddies -- with wives and children in tow -- discover why age does not, necessarily, equal maturity.')
    movie5 = Movie(title= 'Titanic', year=1997, genre='Romance', description='Plot: James Camerons "Titanic" is an epic, action-packed romance set against the ill-fated maiden voyage of the R.M.S. Titanic; the pride and joy of the White Star Line and, at the time, the largest moving object ever built. She was the most luxurious liner of her era -- the ""ship of dreams"" -- which ultimately carried over 1,500 people to their death in the ice cold waters of the North Atlantic in the early hours of April 15, 1912.')
    sandler = Actor(actor_name='Adam Sandler', age=52, role='Danny Maccabee', movie = movie1)
    jolie = Actor(actor_name='Angelina Jolie', age=43, role='Maleficent', movie = movie2)
    pitt = Actor(actor_name='Brad Pitt', age=55, role='John Smith', movie = movie3)
    rock = Actor(actor_name='Chris Rock', age=52, role='Kurt McKenzie', movie = movie4)
    dicaprio = Actor(actor_name='Leonardo DiCaprio', age=44, role='Jack Dawson', movie = movie5)
    db.session.add(movie1)
    db.session.add(movie2)
    db.session.add(movie3)
    db.session.add(movie4)
    db.session.add(movie5)
    db.session.add(sandler)
    db.session.add(jolie)
    db.session.add(pitt)
    db.session.add(rock)
    db.session.add(dicaprio)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
