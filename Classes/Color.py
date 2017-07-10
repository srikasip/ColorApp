import Ada_Utilities as au
from sqlalchemy.orm import sessionmaker, session
import Classes.ObjectsFile
from Classes.ObjectsFile import Color, Person, ENGINE, BASE, APPNAME

class ColorController:
	def __init__(self):
		Session = sessionmaker(bind=ENGINE)
		self.session = Session()

	def selectAll(self):
		allColor = self.session.query(Color).all()
		return allColor
	def selectbyID(self, send_id):
		oneColor = self.session.query(Color).filter(Color.ada_id == send_id)
		return oneColor
	def selectbyID(self, send_id):
		oneColor = self.session.query(Color).filter(Color.ada_id == send_id).delete()
		self.session.commit()


class ColorViewer:
	def __init__(self):
		pass

	def insertOne(self):
		htmlSnippet = "<form>"
		htmlSnippet = "</form>"

	def viewAll(self):
		colorController = ColorController()
		allColors = colorController.selectAll()

		htmlSnippet = "<table>\n"
		htmlSnippet += "\t<tr>\n"
		htmlSnippet += "\t\t<th>Id</th>\n"
		htmlSnippet += "\t\t<th>Color</th>\n"
		htmlSnippet += "\t\t<th>Name</th>\n"
		htmlSnippet += "\t</tr>\n"

		for a_color in allColors:
			htmlSnippet += "\t<tr>\n"
			htmlSnippet += "\t\t<td>"+a_color.ada_id+"</td>\n"
			htmlSnippet += "\t\t<td>"+a_color.color+"</td>\n"
			htmlSnippet += "\t\t<td>"+a_color.name+"</td>\n"
			htmlSnippet += "\t</tr>\n"

		htmlSnippet += "</table>\n"

		return htmlSnippet
