import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


user_character_favorites = Table('user_character_favorites', Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('character_id', Integer, ForeignKey('character.id'), primary_key=True)
)


user_planet_favorites = Table('user_planet_favorites', Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('planet_id', Integer, ForeignKey('planet.id'), primary_key=True)
)


user_vehicle_favorites = Table('user_vehicle_favorites', Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('vehicle_id', Integer, ForeignKey('vehicle.id'), primary_key=True)
)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    surname = Column(String(250), nullable=False)
    
    
    favorite_characters = relationship('Character', secondary=user_character_favorites, back_populates='favorited_by')
    favorite_planets = relationship('Planet', secondary=user_planet_favorites, back_populates='favorited_by')
    favorite_vehicles = relationship('Vehicle', secondary=user_vehicle_favorites, back_populates='favorited_by')

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer)  
    mass = Column(Integer)    
    hair_color = Column(String(50))  
    skin_color = Column(String(50))   
    eye_color = Column(String(50))   
    birth_year = Column(String(50))   
    gender = Column(String(50))        
    homeworld_id = Column(Integer, ForeignKey('planet.id')) 
    homeworld = relationship('Planet')  
    
    
    favorited_by = relationship('User', secondary=user_character_favorites, back_populates='favorite_characters')

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    rotation_period = Column(Integer)   
    orbital_period = Column(Integer)     
    diameter = Column(Integer)            
    climate = Column(String(250))         
    gravity = Column(String(250))         
    terrain = Column(String(250))         
    population = Column(Integer)          

    
    favorited_by = relationship('User', secondary=user_planet_favorites, back_populates='favorite_planets')

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250))         
    manufacturer = Column(String(250))   
    cost_in_credits = Column(Integer)   
    length = Column(Integer)            
    max_atmosphering_speed = Column(Integer)  
    crew = Column(Integer)               
    passengers = Column(Integer)         
    cargo_capacity = Column(Integer)      
    consumables = Column(String(250))     
    vehicle_class = Column(String(250))   

  
    favorited_by = relationship('User', secondary=user_vehicle_favorites, back_populates='favorite_vehicles')

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'), nullable=True)

    user = relationship('User')
    character = relationship('Character')
    planet = relationship('Planet')
    vehicle = relationship('Vehicle')

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
