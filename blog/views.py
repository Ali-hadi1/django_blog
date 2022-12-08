from datetime import date

from django.shortcuts import render

# Create your views here.
all_posts = [
    {
        'slug': 'hike-in-the-mountains',
        'image': 'image2.jpg',
        'author': 'Herry Potter',
        'date': date(2021, 7, 21),
        'title': 'Mountain Hiking',
        'excerpt': 'there\'s nothing like the views you get when hiking in the mountains! And I wasn\'t even prepared for what happened whilst I was enjoying the view!',
        'content': '''
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis arcu arcu, tincidunt nec lorem sed,
             vulputate facilisis felis. Sed lacus elit, porta et risus quis, faucibus ornare odio. 

            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis arcu arcu, tincidunt nec lorem sed,
             vulputate facilisis felis. Sed lacus elit, porta et risus quis, faucibus ornare odio. 

            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis arcu arcu, tincidunt nec lorem sed,
             vulputate facilisis felis. Sed lacus elit, porta et risus quis, faucibus ornare odio. 
        '''
    },
    {
        'slug': 'programming-is-fun',
        'image': 'code.jpeg',
        'author': 'Herry Potter',
        'date': date(2022, 7, 21),
        'title': 'Programming is Great!',
        'excerpt': 'there\'s nothing like the views you get when hiking in the mountains! And I wasn\'t even prepared for what happened whilst I was enjoying the view!',
        'content': '''
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis arcu arcu, tincidunt nec lorem sed,
             vulputate facilisis felis. Sed lacus elit, porta et risus quis, faucibus ornare odio. 

            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis arcu arcu, tincidunt nec lorem sed,
             vulputate facilisis felis. Sed lacus elit, porta et risus quis, faucibus ornare odio. 

            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis arcu arcu, tincidunt nec lorem sed,
             vulputate facilisis felis. Sed lacus elit, porta et risus quis, faucibus ornare odio. 
        '''
    },
    {
        'slug': 'into-the-woods',
        'image': 'wood.jpg',
        'author': 'Herry Potter',
        'date': date(2020, 7, 2),
        'title': 'Nature At Its Best!',
        'excerpt': 'there\'s nothing like the views you get when hiking in the mountains! And I wasn\'t even prepared for what happened whilst I was enjoying the view!',
        'content': '''
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis arcu arcu, tincidunt nec lorem sed,
             vulputate facilisis felis. Sed lacus elit, porta et risus quis, faucibus ornare odio. 

            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis arcu arcu, tincidunt nec lorem sed,
             vulputate facilisis felis. Sed lacus elit, porta et risus quis, faucibus ornare odio. 

            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis arcu arcu, tincidunt nec lorem sed,
             vulputate facilisis felis. Sed lacus elit, porta et risus quis, faucibus ornare odio. 
        '''
    }
]

def get_date(post):
    return post.get('date')

def index(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', {'posts': latest_posts})

def posts(request):
    return render(request, 'blog/posts.html', {'posts': all_posts})

def post_details(request, slug):
    post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-details.html', { 'post': post })