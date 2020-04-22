class Etudiant:

	num_of_etudiants = 0
	
	def __init__(self, first, last, email, score):
		self.first = first
		self.last = last

		self.email = email

		self.score = score

		Etudiant.num_of_etudiants += 1

	def fullname(self):
		return self.first + ' ' + self.last



etudiant_01 = Etudiant('Antoine', "Flynn", "aflynn@college.ca", 80 )
etudiant_02 = Etudiant('Derek', "Cotton", "dcotton@college.ca", 73)


print(Etudiant.num_of_etudiants)


