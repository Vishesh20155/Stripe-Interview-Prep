from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

# Create a model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    content = db.Column(db.String(255))

    def __repr__(self):
        return f"<Post {self.title}>"

# Create a schema    
class PostSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "content")
        model = Post    # This Post is the post class
        
post_schema = PostSchema()
posts_schema = PostSchema(many=True)

# Create API resource list
class PostListResource(Resource):
    def get(self):
        posts = Post.query.all()
        return posts_schema.dump(posts)
    
    def post(self): # This is the POST method
        new_post = Post(
            title = request.form['title'],
            content = request.form['content']
        )
        db.session.add(new_post)
        db.session.commit()
        
        x = post_schema.dump(new_post)
        return x
    
class PostResource(Resource):
    def get(self, post_id):
        post = Post.query.get_or_404(post_id)
        return post_schema.dump(post)
    
    def patch(self, post_id):
        post = Post.query.get_or_404(post_id)
        
        if 'title' in request.form:
            post.title = request.form['title']
        
        if 'content' in request.form:
            post.content = request.form['content']
            
        db.session.commit()
        return post_schema.dump(post)
    
    def put(self, post_id):
        post = Post.query.get(post_id)

        if post is None:
            # If the post does not exist, create a new one
            title = request.form['title']
            content = request.form['content']

            if not title or not content:
                return {'message': 'Title and content are required'}, 400

            new_post = Post(title=title, content=content)
            db.session.add(new_post)
            db.session.commit()

            return post_schema.dump(new_post), 201

        # If the post exists, update it
        post_data = request.get_json()
        if 'title' in post_data:
            post.title = post_data['title']
        if 'content' in post_data:
            post.content = post_data['content']

        db.session.commit()
        return post_schema.dump(post)
    
    
    def delete(self, post_id):
        post = Post.query.get_or_404(post_id)
        db.session.delete(post)
        db.session.commit()
        return "", 204
        
    
class HomePage(Resource):
    def get(self):
        return "Hello"
    
api.add_resource(PostListResource, '/posts')
api.add_resource(PostResource, '/posts/<int:post_id>')
api.add_resource(HomePage, '/')



if __name__ == '__main__':
    app.run(debug=True)