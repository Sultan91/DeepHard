# japronto based web server
to run application:

docker-compose up

### Available requests
- '0.0.0.0:8888/' - GET returns async JSON response
- '0.0.0.0:8888/event' - POST with JSON body like this: 
{
	"id":1,
	"label": "view"
}


