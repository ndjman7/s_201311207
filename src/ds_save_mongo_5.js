use myDB
show dbs
show tables
db.RaDaeJin.insert({"Persons":[{"id":"405", "이름":"js1"},{"id":"406", "이름":"js2"}]})
db.RaDaeJin.find({"Persons.이름": "js2"}, {"Persons.$":1}).pretty()