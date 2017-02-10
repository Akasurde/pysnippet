name = "Abhijeet"

print("%s is good boy" % (name))

print("{0} is good boy".format(name))

print("{student_name} is good boy".format(student_name=name))

err = {"error_count" : 1 }

print("We found %(error_count)d errors" % err)
