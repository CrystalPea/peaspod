from app import app
from flask import render_template


@app.route('/')
def homepage():
    return render_template('index.html', images=[
        {
            "url": "https://64.media.tumblr.com/b1cb0bfa0fdf0a31106b59cde54f285a/tumblr_pu80heYGrZ1sm6okzo1_500.png",
            "alt": "KK in her party costume"
        },
        {
            "url": "https://64.media.tumblr.com/2f6977c2c94fdf9d214201dc8e33ebdb/tumblr_pu80heYGrZ1sm6okzo2_500.png",
            "alt": "Paul in his party costume"
        },
        {
            "url": "https://64.media.tumblr.com/64fb398518ddbe215874418c46cc3b57/tumblr_nzorf6g1ty1sm6okzo1_500.jpg",
            "alt": "Flower sticks resembling a flower"
        }
    ])
