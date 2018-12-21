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


class Category(Base):
	__tablename__ = 'category'

	name = Column(String(250), primary_key=True, nullable=False)

	@property
	def serialize(self):
		"""Return object data in easily serializeable format"""
		return {
			'name': self.name,
		}


class Item(Base):
    __tablename__ = 'item'

    title = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    fk_cat_name = Column(String(250), ForeignKey('category.name'))
    category = relationship(Category)
    date_added = Column(String(10), nullable=False)
    
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'fk_cat_name': self.fk_cat_name,
            'description': self.description,
            'id': self.id,
            'title': self.title,
        }

engine = create_engine('sqlite:///catalogproject.db')

Base.metadata.create_all(engine)