from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_setup import User, Category, Item

engine = create_engine('sqlite:///catalogproject.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Dinesheo Bedio", email="DinBedio@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Soccer Category & Items 
Category1 = Category(fk_user_id=User1.id, name="Soccer")

session.add(Category1)
session.commit()

Item1 = Item(title="Jersey", description="West Bromwich Albion home top with navy blue & white stripes.",
                     fk_cat_id=Category1.id, fk_user_id=User1.id, date_added="02-01-2018")
session.add(Item1)
session.commit()

Item2 = Item(title="Two Shinguards", description="Padded shinguards for both legs",
                     fk_cat_id=Category1.id, fk_user_id=User1.id, date_added="06-12-2018")

session.add(Item2)
session.commit()

Item3 = Item(title="Shinguards", description="Cushioned shinguards including a spare",
                     fk_cat_id=Category1.id, fk_user_id=User1.id, date_added="09-12-2018")

session.add(Item3)
session.commit()

Item4 = Item(title="Soccer Cleats", description="The finest Soccer Cleats that money can buy",
                     fk_cat_id=Category1.id, fk_user_id=User1.id, date_added="05-30-2018")

session.add(Item4)
session.commit()


# Hockey Category & Items 
Category2 = Category(fk_user_id=User1.id, name="Hockey")

session.add(Category2)
session.commit()

Item1 = Item(title="Stick", description="Red hockey stick",
                     fk_cat_id=Category2.id, fk_user_id=User1.id, date_added="10-10-2018")
session.add(Item1)
session.commit()

# Snowboarding Category & Items 
Category3 = Category(fk_user_id=User1.id, name="Snowboarding")

session.add(Category3)
session.commit()

Item1 = Item(title="Goggles", description="Clear, air-tight goggles for all weather conditions.",
                     fk_cat_id=Category3.id, fk_user_id=User1.id, date_added="11-05-2018")
session.add(Item1)
session.commit()

Item2 = Item(title="Snowboard", description="Large, bright orange snowboard.",
                     fk_cat_id=Category3.id, fk_user_id=User1.id, date_added="06-12-2018")

session.add(Item2)
session.commit()

# Frisbee Category & Items 
Category4 = Category(fk_user_id=User1.id, name="Frisbee")

session.add(Category4)
session.commit()

Item1 = Item(title="Frisbee", description="Bright green frisbee.",
                     fk_cat_id=Category4.id, fk_user_id=User1.id, date_added="03-16-2018")
session.add(Item1)
session.commit()

# Baseball Category & Items 
Category5 = Category(fk_user_id=User1.id, name="Baseball")

session.add(Category5)
session.commit()

Item1 = Item(title="Baseball Bat", description="Pale, wooden baseball bat for all ages.",
                     fk_cat_id=Category5.id, fk_user_id=User1.id, date_added="01-30-2018")
session.add(Item1)
session.commit()

print("added menu items!")