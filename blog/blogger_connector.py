import sys

from oauth2client import client
from googleapiclient import sample_tools


def create_draft_post(blog_id, posts):
    content = {"kind": "blogger#post",
               "id": blog_id,
               "title": "TEST Blog Post via Python",
               "content": "<div><img src='http://socialnewsdaily.com/wp-content/uploads/2014/05/rick-astley-rickrolling.jpg'><img>hello world test</div>"}
    new_post = posts.insert(blogId=blog_id, body=content)
    return new_post.execute()


def update_blog_post(blog_id, post_id, content, posts):
    return


def main(argv):
    service, flags = sample_tools.init(argv, 'blogger', 'v3', __doc__, __file__, scope='https://www.googleapis.com/auth/blogger')

    try:

        users = service.users()
        blogs = service.blogs()
        posts = service.posts()

        # Retrieve this user's profile information
        this_user = users.get(userId='self').execute()
        print('This user\'s display name is: %s' % this_user['displayName'])

        # Retrieve the list of Blogs this user has write privileges on
        this_users_blogs = blogs.listByUser(userId='self').execute()
        for blog in this_users_blogs['items']:
            print('The blog named \'%s\' is at: %s' % (blog['name'], blog['url']))
            # Publish a draft page
            new_post = create_draft_post(blog['id'], posts)
            print(new_post)

        # List the posts for each blog this user has
        for blog in this_users_blogs['items']:
            print('The posts for %s:' % blog['name'])
            request = posts.list(blogId=blog['id'])
            print('The id is: %s' % blog['id'])
            while request != None:
                posts_doc = request.execute()
                if 'items' in posts_doc and not (posts_doc['items'] is None):
                    for post in posts_doc['items']:
                        print('  %s (%s)' % (post['title'], post['url']))
                request = posts.list_next(request, posts_doc)

    except client.AccessTokenRefreshError:
        print('The credentials have been revoked or expired, please re-run'
              'the application to re-authorize')

if __name__ == '__main__':
    main(sys.argv)