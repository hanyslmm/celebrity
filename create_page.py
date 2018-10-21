import webbrowser
import os
import re
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
        <div class="col-md-4">
          <img src="https://i.pinimg.com/originals/23/75/a5/2375a5f598107e9b4d663fc34c83ece5.png" class="title-logo img-fluid img-responsive"/>
        </div>
        <div class="col-md-4">
          <!-- TODO: add login tabs -->
        </div>
        <div class="col-md-4">
          <h1 class="title-super text-right text-uppercase text-thin">Celebrity Home</h1>
          <h4 class="text-right">Famous Celebrities Inspirational Quotes</h4>
        </div>
      </div>
      <div class="row">


    <div class="row jumbotron img-responsive">
      <hr>
    </div>

        <!-- el webaaaya bta3ty  -->


                '''
# A single Celebrity entry html template
profile_content = '''
    <div class="col-md-6 col-lg-4 text-center" data-toggle="modal" data-target="#trailer">
        <img src="{}" class="img-rounded img-fluid" width="342" height="342" alt="cover page">
        <h2>{}</h2>
        <p>Age: {}</p>
        <p>{}</p>
    </div>
                '''
footer = '''
        <div class="col-md-8">
          <blockquote>
            <p>The opportunity we have is to build a secure,
            intelligent platform that solves some of the worlds
            greatest problems at scale. Thats whats possible with
            hundreds of billions of connections and the capabilities
            that we can deliver together.</p>
            <footer>Hany Salama</footer>
          </blockquote>
        </div>
</body>
</html>
        '''


def create_profile_page(users):
    f = open('profile.html', 'w')

    rendered_content = profile_content.format(users[0].poster, users[0].name, users[0].age(), users[0].quote)
    rendered_content_1 = profile_content.format(users[1].poster, users[1].name, users[1].age(), users[1].quote)
    rendered_content_2 = profile_content.format(users[2].poster, users[2].name, users[2].age(), users[2].quote)
    rendered_content_3 = profile_content.format(users[3].poster, users[3].name, users[3].age(), users[3].quote)
    rendered_content_4 = profile_content.format(users[4].poster, users[4].name, users[4].age(), users[4].quote)
    rendered_content_5 = profile_content.format(users[5].poster, users[5].name, users[5].age(), users[5].quote)

    f.write(main_page + rendered_content + rendered_content_1 + rendered_content_2 + rendered_content_3 + rendered_content_4 + rendered_content_5 + footer)
    f.close()
