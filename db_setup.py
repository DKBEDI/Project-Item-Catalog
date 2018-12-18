from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
	__tablename__ = 'user'

	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	email = Column(String(250), nullable=False)
	picture = Column(String(250))


class Category(Base):
	__tablename__ = 'category'

	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	fk_user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)

	@property
	def serialize(self):
		"""Return object data in easily serializeable format"""
		return {
			'name': self.name,
			'id': self.id,
		}


class Item(Base):
    __tablename__ = 'item'

    title = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    fk_cat_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
    fk_user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    date_added = Column(String(10), nullable=False)
    
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'fk_cat_id': self.fk_cat_id,
            'description': self.description,
            'id': self.id,
            'title': self.title,
        }

engine = create_engine('sqlite:///catalogproject.db')

Base.metadata.create_all(engine)