# references: 
    # https://jrvcomputing.wordpress.com/2023/03/29/setting-up-my-personal-website-using-nikola/
    # https://getnikola.com/creating-a-site-not-a-blog-with-nikola.html

NIKOLA_DEBUG=1

DEFAULT_LANG = "en"
THEME = "base-jinja"
TIMEZONE = "Asia/Kolkata"

SITENAME = "Michael Bertagna"

FAVICON = '/flavicon.png'
 
NAVIGATION_LINKS = {
    DEFAULT_LANG: (
        ('Home', '/'),
        ('About', '/about.html'),
        ('Posts', '/posts.html'),
        ('Contact', '/contact.html'),
    )
}

POSTS = (
    ("posts/*.rst", "posts", "post.tmpl"),
    ("posts/*.txt", "posts", "post.tmpl"),
    ("posts/*.html", "posts", "post.tmpl"),
    ("posts/*.ipynb", "posts", "post.tmpl"),
)

PAGES = (
    ("pages/*.rst", "", "page.tmpl"),
    ("pages/*.md", "", "page.tmpl"),
    ("pages/*.txt", "", "page.tmpl"),
    ("pages/*.html", "", "page.tmpl"),
    ("pages/*.ipynb", "", "page.tmpl"),
)

INDEX_PATH = "blog"
 
COMPILERS = {
    "markdown": ['.md', '.mdown', '.markdown'],
    "html": ['.html', '.htm'],
}
METADATA_FORMAT = "YAML"
MARKDOWN_EXTENSIONS = [
    'markdown.extensions.fenced_code',
    'markdown.extensions.codehilite',
    'markdown.extensions.extra']
 
PRETTY_URLS = False
 
# Plugins you don't want to use. Be careful 🙂
DISABLED_PLUGINS = ["redirect", "render_galleries", "render_listings",
                    "render_sources", "render_taxonomies", "robots",
                    "scale_images", "create_bundles", "sitemap"]
# Based on output of "nikola list", the ENABLED_PLUGINS are
#            "copy_assets", "copy_files",
#            "post_render",
#            "render_pages", "render_posts", "render_site"

