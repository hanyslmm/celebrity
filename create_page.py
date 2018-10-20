import webbrowser
import os
import re
"""    <div class="row jumbotron img-responsive">
      <img src="img/Kitchen3.jpg" class="img-responsive img-rounded img-fluid img-thumbnail"
      alt="cover page" />
    </div>
    <div class="row text-muted">
      <h2>Our Smart Solutions</h2>
    </div>
    <div class="row img-responsive text-center">
      <div class="col-md-4">
        <img src="img/mobapp.jpg" class="img-thumbnail img-responsive img-rounded" alt="mobile app"/>
        <h3 class="text-uppercase center">Mobile Application</h3>
        <p>
          this is a paragraph
        </p>
      </div>
      <div class="col-md-4">
        <img src="img/img-2.jpg" class="img-thumbnail img-responsive img-rounded" alt="mobile app"/>
        <h3 class="text-uppercase">Security Camers</h3>
        <p>
          this is a paragraph
        </p>
      </div>
      <div class="col-md-4">
        <img src="img/img-3.jpg" class="img-thumbnail img-responsive img-rounded" alt="mobile app"/>
        <h3 class="text-uppercase">Street Lighting</h3>
        <p>
          this is a paragraph
        </p>
      </div>
    </div>"""

# The main page layout and title bar
main_page = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Celebrity Profile</title>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width,
   initial-scale=1, user-scalable=no">
  <link href="bootstrap.css" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Lato"
   rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Roboto:300,500&amp;subset=greek"
   rel="stylesheet">
</head>

<body>
  <div class="container">
    <div class="row jumbotron img-responsive">
      <hr>
    </div>

        <!-- el webaaaya bta3ty  -->


                '''
# A single Celebrity entry html template
profile_content = '''
    <div class="col-md-6 col-lg-4 text-center" data-toggle="modal" data-target="#trailer">
        <img src="{}" width="342" height="342">
        <h2>{}</h2>
        <p>Age: {}</p>
    </div>
                '''
footer = '''
        <div class="col-md-8">
          <blockquote>
            <p>“The opportunity we have is to build a secure, intelligent platform that solves some of the world’s greatest problems at scale. That’s what’s possible with hundreds of billions of connections and the capabilities that we can deliver together.”</p>
            <footer>Hany Salama</footer>
          </blockquote>
        </div>
</body>
</html>
'''


def create_profile_page(users):
    f = open('profile.html', 'w')
    
    rendered_content = profile_content.format(users[0].poster, users[0].name, users[0].age())
    rendered_content_1 = profile_content.format(users[1].poster, users[1].name, users[1].age())
    rendered_content_2 = profile_content.format(users[2].poster, users[2].name, users[2].age())
    rendered_content_3 = profile_content.format(users[3].poster, users[3].name, users[3].age())
    rendered_content_4 = profile_content.format(users[4].poster, users[4].name, users[4].age())

    f.write(main_page + rendered_content + rendered_content_1 + rendered_content_2 + rendered_content_3 + rendered_content_4 + footer)
    f.close()
