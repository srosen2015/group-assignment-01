from flask_script import Manager
from project import app, db

manager = Manager(app)


@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    x = X()
    movie1 = Movie(title= 'The Lion King', description='Plot: tells the story of Simba, a young lion who is to succeed his father, Mufasa, as King of the Pride Lands; however, after Simbas uncle Scar, murders Mufasa, Simba is manipulated into thinking he was responsible and flees into exile. Upon maturation living with two wastrels, Simba is given some valuable perspective from his childhood friend, Nala, and his shaman, Rafiki, before returning to challenge Scar to end his tyranny and take his place in the Circle of Life as the rightful King.')
    movie2 = Movie(title='Mulan', description='Plot: Fearful that her ailing father will be drafted into the Chinese military, Mulan (Ming-Na Wen) takes his spot -- though, as a girl living under a patriarchal regime, she is technically unqualified to serve.')
    movie3 = Movie(title='Moana', description='An adventurous teenager sails out on a daring mission to save her people.')
    movie4 = Movie(title='Frozen', description='When their kingdom becomes trapped in perpetual winter, fearless Anna (Kristen Bell) joins forces with mountaineer Kristoff (Jonathan Groff) and his reindeer sidekick to find Annas sister, Snow Queen Elsa (Idina Menzel), and break her icy spell.')
    movie5 = Movie(title='Cinderella', description='With a wicked stepmother (Eleanor Audley) and two jealous stepsisters (Rhoda Williams, Lucille Bliss) who keep her enslaved and in rags, Cinderella (Ilene Woods) stands no chance of attending the royal ball.')

    db.session.add(movie1)
    db.session.add(movie2)
    db.session.add(movie3)
    db.session.add(movie4)
    db.session.add(movie5)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
