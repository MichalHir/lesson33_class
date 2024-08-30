from models import Pet

pet1 = Pet("Dixie",8,"https://t4.ftcdn.net/jpg/01/99/00/79/360_F_199007925_NolyRdRrdYqUAGdVZV38P4WX8pYfBaRP.jpg","Dog")
pet2 = Pet("Mitzi",2,"https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg","Cat")

# print ("pet1:",pet1.name,"age:",pet1.age)
# print ("pet2 is",pet2.name,"age:",pet2.age)


pet2.age = 3
pet2.name = "Bobby"

print(pet1)
print(pet2)
