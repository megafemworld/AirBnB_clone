# AirBnB Clone

This is a simple command-line interface (CLI) application that simulates some functionalities of the AirBnB web application. The project allows for the creation, storage, and manipulation of user, state, city, amenity, place, and review objects.

## Description of the Project

The AirBnB clone project is a console-based application written in Python. It utilizes Object-Oriented Programming (OOP) concepts to manage different types of objects such as users, places, states, cities, amenities, and reviews. The project includes a custom storage engine to serialize and deserialize object data to and from a JSON file.

## Description of the Command Interpreter

The command interpreter is the central part of the project. It allows users to interact with the application by typing commands to create, show, update, and destroy objects.

### Features

- **Create new objects**: Create instances of various classes such as `User`, `State`, `City`, `Amenity`, `Place`, and `Review`.
- **Show objects**: Display the string representation of an instance based on its class name and ID.
- **Update objects**: Modify attributes of existing instances.
- **Destroy objects**: Delete instances based on their class name and ID.
- **All objects**: Display all instances of a class or all instances in general.

### How to Start the Command Interpreter

To start the command interpreter, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/megafemworld/AirBnB_clone.git
    cd AirBnB_clone
    ```

2. **Make the console script executable** (if not already):
    ```sh
    chmod +x console.py
    ```

3. **Run the console**:
    ```sh
    ./console.py
    ```

### How to Use the Command Interpreter

Once the command interpreter is running, you can use the following commands:

- **Create a new object**:
    ```sh
    (hbnb) create <ClassName>
    ```
    Example:
    ```sh
    (hbnb) create User
    ```

- **Show an object**:
    ```sh
    (hbnb) show <ClassName> <id>
    ```
    Example:
    ```sh
    (hbnb) show User 1234-5678-9012
    ```

- **Destroy an object**:
    ```sh
    (hbnb) destroy <ClassName> <id>
    ```
    Example:
    ```sh
    (hbnb) destroy User 1234-5678-9012
    ```

- **Update an object**:
    ```sh
    (hbnb) update <ClassName> <id> <attribute name> "<attribute value>"
    ```
    Example:
    ```sh
    (hbnb) update User 1234-5678-9012 email "airbnb@mail.com"
    ```

- **Show all objects**:
    ```sh
    (hbnb) all <ClassName>
    ```
    Example:
    ```sh
    (hbnb) all User
    ```

- **Show all objects (all classes)**:
    ```sh
    (hbnb) all
    ```

- **Help command**:
    ```sh
    (hbnb) help
    ```

### Examples

Here are some example interactions with the command interpreter:

```sh
$ ./console.py
(hbnb) create User
d5d7d01c-89e0-4e33-a3fb-9f4f3c7b9451
(hbnb) show User d5d7d01c-89e0-4e33-a3fb-9f4f3c7b9451
[User] (d5d7d01c-89e0-4e33-a3fb-9f4f3c7b9451) {'id': 'd5d7d01c-89e0-4e33-a3fb-9f4f3c7b9451', 'created_at': datetime.datetime(...), 'updated_at': datetime.datetime(...)}
(hbnb) update User d5d7d01c-89e0-4e33-a3fb-9f4f3c7b9451 email "airbnb@mail.com"
(hbnb) show User d5d7d01c-89e0-4e33-a3fb-9f4f3c7b9451
[User] (d5d7d01c-89e0-4e33-a3fb-9f4f3c7b9451) {'email': 'airbnb@mail.com', 'id': 'd5d7d01c-89e0-4e33-a3fb-9f4f3c7b9451', 'created_at': datetime.datetime(...), 'updated_at': datetime.datetime(...)}
(hbnb) all User
["[User] (d5d7d01c-89e0-4e33-a3fb-9f4f3c7b9451) {'email': 'airbnb@mail.com', 'id': 'd5d7d01c-89e0-4e33-a3fb-9f4f3c7b9451', 'created_at': datetime.datetime(...), 'updated_at': datetime.datetime(...)}"]
(hbnb) destroy User d5d7d01c-89e0-4e33-a3fb-9f4f3c7b9451

