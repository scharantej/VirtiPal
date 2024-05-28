## Flask Application Design

### HTML Files

- **index.html**: This will be the home page of the application. It will contain the necessary HTML and JavaScript code to allow the user to interact with the pet simulator.
- **pet.html**: This page will display the virtual pet. It will receive data from the Flask backend and update the pet's appearance and actions accordingly.

### Routes

- **`/`**: This route will handle requests for the home page. It will render the `index.html` file.
- **`/pet`**: This route will handle requests to create or update the virtual pet. It will receive data from the user via a POST request and return a JSON response with the updated pet information.
- **`/pet/action`**: This route will handle requests to perform an action with the pet. It will receive an action name as a parameter via a GET request and return a JSON response with the result of the action.
- **`/pet/describe`**: This route will handle requests to describe the pet. It will receive a description as a parameter via a POST request and return a JSON response with the updated pet's description.
- **`/pet/learn`**: This route will handle requests to teach the pet a new trick. It will receive a trick name as a parameter via a POST request and return a JSON response with the updated pet's knowledge.