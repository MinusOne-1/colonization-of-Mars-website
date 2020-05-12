

from data.Jobs import Jobs
from data.User import User
from data import db_session



astrons = [["Scott", "Ridley", 21, "captain", "research engineer", "module_1", "scott_chief@mars.org", "cap"], #капитан
           ["Vincent", "Gog", 27, "colonist", "doctor", "module_1", "two_ears_human@mars.org", "nope"], #колонист 1
           ["Nataly", "Tools", 26, "colonist", "navigator", "module_1", "ToolsToons@mars.org", "omg_imonMars"], #колонист 2
           ["Alex", "Thdfgsdfer", 29, "colonist", "pilot", "module_1", "mrSurrealSurname2020@mars.org", "ehhhhh"]] #колонист 3
for i in range(3):
    user = User()
    user.surname = astrons[i][0]
    user.name = astrons[i][1]
    user.age = astrons[i][2]
    user.position = astrons[i][3]
    user.speciality = astrons[i][4]
    user.address = astrons[i][5]
    user.email = astrons[i][6]
    user.hashed_password = astrons[i][7]
    session.add(user)
