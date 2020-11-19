db = new Mongo().getDB('{{cookiecutter.mongodb_database}}');
db.createCollection('{{cookiecutter.mongodb_collection}}');

db.createUser({
    user: '{{cookiecutter.mongodb_new_username}}',
    pwd: '{{cookiecutter.mongodb_new_username_password}}',
    roles: [
        {
            role: 'readWrite',
            db: '{{cookiecutter.mongodb_database}}',
        },
    ],
});