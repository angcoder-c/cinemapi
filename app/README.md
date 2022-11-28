 # Routes API
 
 ## Public
> Public routes accessible by `GET` method.

- `/` : index route
Redirects to `/movies` path, returns status code `302`.

- `/movies/` : list of movies in billboard
Returns a list of json objects with the properties of each movie in theaters, returns the status code `200`.

- `/logout/` 
Closes the user's session if it is active, if it is not it returns an error, returns the status code `200`.

- `/tickets/` : list of tickets sold
Returns a list of tickets sold, the show they were reserved for, and the corresponding movie, returns the status code `200`.

- `/shows/` : list of available shows
Returns a list of available shows and corresponding movies, returns the status code `200`.

> Public routes accessible by `POST` method.

- `/signin/` : signin path
Receives a json in the body of the message, with the necessary fields for the registration in the database, and returns a json with a confirmation message.

```json
{
        "firstname" : "Firstname", 
        "lastname" : "Lastname", 
        "username" : "username", 
        "password" : "123", 
        "email" : "username@mail.com",
        "phone" : "12345678", 
        "phone_country_code" : "502"
}
```

- `/login/` : login path
Receives a json in the body of the message, with the necessary fields for user login, and returns a json with an authorization token.

```json
{
        "password" : "123", 
        "email" : "username@mail.com",
}
```

## Private

> Protected routes accessible by `GET` method.

- `/tickets/my/` : User-purchased tickets
Returns the tickets purchased by the user, as long as the user is logged in and has the authentication token.

> Protected routes accessible by `POST` method.

`/tickets/buy/` : endpoint of ticket purchase
Receives a json object in the request body and returns a purchase confirmation message and purchased ticket information.

```json
{
        "movie_id" : 1, 
        "seating" : ["A03", "B03"], 
        "show_id" : 1
}
```
`/tickets/cancel/` : endpoint to cancel the purchase of tickets
Receives a json object in the request body, containing the id of the ticket to cancel, and returns a confirmation or error message, depending on the cancellation date.

```json
{
    "ticket_id" : [int]
}
```