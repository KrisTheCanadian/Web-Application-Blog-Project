from flask import Blueprint, request, render_template

from app.models import User, Post

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=6)
    return render_template('home.html', posts=posts)


@main.route('/about')
def about():
    users = User.query.order_by(User.username)
    posts = []
    count = []
    for user in users:
        q = Post.query.filter_by(author=user).order_by(Post.date_posted.desc())
        posts.append(q.first())
        count.append(q.count())
    return render_template('about.html', title='About', users=users, posts=posts, count=count)
