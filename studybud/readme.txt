to render a database,(although django in settings- apps there is default databases) we are going to go to   run  migrations using

python manage.py migrate
 
 the migrations have been applied ,there is no error in the terminal when you run the server


in models.py we are going to create our tables

                we are going to create python classes, the class we create we are going to create a tables
                 every instance we create 

                 for every model created  make    migrations

                 ie.......python manage.py makemigrations
 2  new python file are  created 

 after that migrate,applys the new file in base

 integrate room in the database by going to  admin ----> steps are included in that file

 with the database beng created , rooms created in the database can be seen in the frontend this is by :
  
                1.import model to query
                2.make a query to the database:
                       queryset   =  modelname.objects.all()----> .get(),.filter(), .exclude()
                         |                  |        |
                         variable that     this is    model objects
                         hols response     model name    attribute


             note that models by default have id genertaed for them , hence the  rooms  created in  database will be the front part and noot the rooms in the views.py



CRUWD---->create ,read,update, write ,delete 
create a template in base ---> room_form.html

in the home.html a user can create room room_form 

instead of manuall9y filling the form , we can create a new python fle, there is abstraction



<!--
   {% for room in rooms %}
    <div>
        only shows the edit and delete buttons to the roomcreator
        {%if request.user == room.host%}
         <a href="{% url 'update_room' room.id %}">Edit</a>
         <a href="{% url 'delete-room' room.id %}">Delete</a> 
         {% endif %}  

       render username to the  site,you can also query upwards to tthe parent it
       <a href="{% url 'user-profile' room.host.id %}">@{{room.host.username }}</a>
       
        add links,pass the url  
       <h4>{{room.id}} -- <a href="{% url 'room' room.id  %}">{{room.name}}</a></h4>
          <small>{{room.topic.name}}</small>
        <hr>            
    </div>
    {%  endfor %}

 -->