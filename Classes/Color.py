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

  def insertOne(self, params):
    try:
      newColor = Color(params["color"], params["name"])
      self.session.add(newColor)
      self.session.commit()
      return True

    except:
      return False


class ColorViewer:
  def __init__(self):
    pass

  def insertOneForm(self):
    htmlSnippet = ""
    htmlSnippet += '<div id="div_colorForm">\n'
    htmlSnippet += '\t<label class="form_label" for="txt_color">Color:</label>\n'
    htmlSnippet += '\t<input type="text" class="form_text" id="txt_color" data-param="color" val="" />\n'
    htmlSnippet += '\n'
    htmlSnippet += '\t<label class="form_label" for="txt_name">Name:</label>\n'
    htmlSnippet += '\t<input type="text" class="form_text" id="txt_name" data-param="name" val="" />\n'
    htmlSnippet += '\n'
    htmlSnippet += '\t<button id="btn_submitColor" class="submitButton">Submit</button>\n'
    htmlSnippet += '\n'
    htmlSnippet += '\t<script>\n'
    htmlSnippet += '\t\t$(document).ready(function(){\n'
    htmlSnippet += '\t\t\t$("#btn_submitColor").click(function(){\n'
    htmlSnippet += '\t\t\t\tvar nameVal = $("#txt_name").val();\n'
    htmlSnippet += '\t\t\t\tvar colorVal = $("#txt_color").val();\n'
    htmlSnippet += '\n'
    htmlSnippet += '\t\t\t\tif(colorVal != "" && nameVal != "")\n'
    htmlSnippet += '\t\t\t\t{\n'
    htmlSnippet += '\t\t\t\t\t$.ajax({\n'
    htmlSnippet += '\t\t\t\t\t\tmethod: "POST",\n'
    htmlSnippet += '\t\t\t\t\t\turl: "color",\n'
    htmlSnippet += '\t\t\t\t\t\tdata: {\n'
    htmlSnippet += '\t\t\t\t\t\t"values": { "name": nameVal, "color": colorVal},\n'
    htmlSnippet += '\t\t\t\t\t\t"call" : "insert"\n'
    htmlSnippet += '\t\t\t\t\t}\n'
    htmlSnippet += '\t\t\t\t})\n'
    htmlSnippet += '\t\t\t\t.done(function(msg) {\n'
    htmlSnippet += '\t\t\t\t\tif(msg == "Successful Insertion")\n'
    htmlSnippet += '\t\t\t\t\t{\n'
    htmlSnippet += '\t\t\t\t\t\twindow.location.replace("/color");\n'
    htmlSnippet += '\t\t\t\t\t}\n'
    htmlSnippet += '\t\t\t\telse\n'
    htmlSnippet += '\t\t\t\t{\n'
    htmlSnippet += '\t\t\t\t\talert("Insertion Failed");\n'
    htmlSnippet += '\t\t\t\t\t$("#txt_name").val("");\n'
    htmlSnippet += '\t\t\t\t\t$("#txt_color").val("");\n'
    htmlSnippet += '\t\t\t\t}\n'
    htmlSnippet += '\t\t\t});\n'
    htmlSnippet += '\t\t}\n'
    htmlSnippet += '\t\t});\n'
    htmlSnippet += '\t\t});\n'
    htmlSnippet += '\t</script>\n'
    htmlSnippet += '</div>\n'

    return htmlSnippet

  def insertOneLoad(self, params):
    colorController = ColorController()
    returnVal = colorController.insertOne(params["values"])

    if returnVal:
      sendData = "Successful Insertion"
    else:
      sendData = "Unsuccessful Insertion"

    return sendData

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
      htmlSnippet += "\t\t<td>"+str(a_color.ada_id)+"</td>\n"
      htmlSnippet += "\t\t<td>"+a_color.color+"</td>\n"
      htmlSnippet += "\t\t<td>"+a_color.name+"</td>\n"
      htmlSnippet += "\t</tr>\n"

    htmlSnippet += "</table>\n"

    return htmlSnippet
