
from flask_restful import Resource, Api
from flask import Flask, jsonify, request, make_response
import jwt
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from functools import wraps
from models import *
import datetime

class Login(Resource):
      
    # Corresponds to POST request
    def post(self):
          
        username = request.json["username"]
        password = request.json["password"]

        user = db.session.query(User).filter(User.username == username,User.password == password).first()
    
        formattedUser = {
            'id': user.id,
            'name': user.username, 
            'email': user.email
        }
        if user:
            access_token = create_access_token(identity=user.id)
            return make_response(jsonify({'message':"Login Succeeded!", 'access_token':access_token, 'user': formattedUser}),200)
        else:
            return make_response(jsonify({'message':"Bad Email or Password"}),401)
                
        
class Register(Resource):
    def post(self):
        
        username = request.json["username"]
        password = request.json["password"]
        email = request.json["email"]
        
        new_user = User(username=username, password=password, email=email)
        try:
            # msg = "Hi " + username + ", you are successfully registered!!"
            db.session.add(new_user)
            db.session.commit()
        except:
            raise
        
        return make_response(jsonify({'message':"Register Succeeded!", 'success': True}),200)
    
class Decks(Resource):
    @jwt_required()
    def get(self):
        
        current_user_id = get_jwt_identity()
        
        print("Current user:", current_user_id)
        decks = db.session.query(Deck).filter(Deck.user_id == current_user_id).all()
        
        formattedDecks = []
        for d in decks:
            formattedDecks.append({
                'id': d.id,
                'name': d.name,
                'last_reviewed': d.last_reviewed.date().strftime('%m/%d/%Y'),
                'score': d.score
        })
          
        print("Formatted Decks:", formattedDecks)
        return make_response(jsonify(formattedDecks), 200)
    
    @jwt_required()
    def post(self):
        
        current_user_id = get_jwt_identity()
        
        name = request.get_json()["deck_name"] 
        
        new_deck = Deck(name=name,user_id=current_user_id)
        try:
            db.session.add(new_deck)
            db.session.commit()
        except:
            raise
        
        return make_response(jsonify({'message':"New Deck added successfully!",'success': True}),200)
    
    @jwt_required()
    def delete(self,deck_id):
        current_user_id = get_jwt_identity()
        
        deck = Deck.query.get(deck_id)
        
        try:
            db.session.delete(deck)
            db.session.commit()
        except:
            raise
        
        return make_response(jsonify({'message':"Deck deleted successfully!",'success': True}),200)
    
    @jwt_required()
    def put(self,deck_id):
        current_user_id = get_jwt_identity()
        deck = Deck.query.get(deck_id)
        
        if deck.user_id != current_user_id:
            return make_response(jsonify({'message':"this deck doesnot belong to current user",'success':'False'}),200)
        
        deckNewName = request.get_json()["deck_name"]        
        deck.name= deckNewName
        db.session.commit()
        
        return make_response(jsonify({'message':"Deck name changed successfully!",'success':'True'}),200)
        
class Cards(Resource):
    @jwt_required()
    def get(self,deck_id):
        # deck_id = request.json["deck_id"]
        
        cards = db.session.query(Card).filter(Card.deck_id == deck_id).all()
        
        formattedCards = []
        for c in cards:
            formattedCards.append({
                'id': c.id,
                'front': c.front,
                'back': c.back
        })
                
        return make_response(jsonify(formattedCards),200)
    
    @jwt_required()
    def post(self):
        
        front = request.json["front"]
        back = request.json["back"]
        deck_id = request.json["deck_id"]
        
        try:
            new_card = Card(front=front,back=back,deck_id=deck_id)
            db.session.add(new_card)
            db.session.commit()
        except:
            raise
        
        return make_response(jsonify({'message':"New Card added successfully!", 'success': True}),200)
    
    @jwt_required()
    def delete(self,card_id):
         
        card = Card.query.get(card_id)
        
        try:
            db.session.delete(card)
            db.session.commit()
        except:
            raise
        
        return make_response(jsonify({'message':"Card deleted successfully!", 'success': True}),200)
    
    @jwt_required()
    def put(self,card_id):
        current_user_id = get_jwt_identity()
        
        card = Card.query.get(card_id)
        
        deck = Deck.query.get(card.deck_id)
        
        if deck.user_id != current_user_id:
            return make_response(jsonify({'message':"this card doesnot belong to current user",'success':'False'}),200)
        
        front = request.get_json()["front"]
        back = request.get_json()["back"]  
             
        card.front = front
        card.back = back
        db.session.commit()
        
        return make_response(jsonify({'message':"Card changed successfully!",'success':'True'}),200)
    
    
    
class Scores(Resource):
    @jwt_required()
    def put(self,deck_id):
        current_user_id = get_jwt_identity()
            
        deck = Deck.query.get(deck_id)
            
        if deck.user_id != current_user_id:
            return make_response(jsonify({'message':"this card doesnot belong to current user",'success':'False'}),200)
        
        deck.score = request.get_json()["score"]
        deck.last_reviewed = datetime.date.today()
        db.session.commit()
            
        return make_response(jsonify({'message':"Score updated successfully!",'success':'True'}),200)
            
            
            
    
        
        
        
        
        
    

        
        
        
    
        
        
        
        
        
        