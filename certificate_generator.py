from PIL import Image, ImageDraw, ImageFont
import configparser

class Certificate:
	"""
	Defines an certificate with the following properties:

    Attributes:
        name: A string representing the certificate reciever's name.
        course: A string representing the name of the course enrolled in.
        date: A string representing the date of issue of certificate.
		output: A string representing the name of the output file that will be generated (has to be an image file).
	"""
	def __init__(self,name,course,date,output):
		"""

		Creates and returns an instace of certificate with the attributes specified

		"""
		self.name = name
		self.course = course
		self.date = date
		self.output = output

	def configure(self):
		"""

		Configures the settings and properties necessary to create the certificate.
		This function imports the configurations from the "config.txt" file.
		The different configuration options are discussed in the documentation

		"""
		config = configparser.ConfigParser()
		try:
			config.read("config.txt")
			self.cert = config['SETTINGS']['TEMPLATE']
			self.font1 = config['NAME']['NAME_FONT']
			self.color1 = config['NAME']['NAME_COLOR']
			self.size1 = int(config['NAME']['NAME_FONT_SIZE'])
			self.size2 = int(config['EVENT']['EVENT_FONT_SIZE'])
			self.font2 = config['EVENT']['EVENT_FONT']
			self.color2 = config['EVENT']['EVENT_COLOR']
			self.size3 = int(config['DATE']['DATE_FONT_SIZE'])
			self.font3 = config['DATE']['DATE_FONT']
			self.color3 = config['DATE']['DATE_COLOR']
			self.x1 = int(config['NAME']['NAME_X'])
			self.y1 = int(config['NAME']['NAME_y'])
			self.width1 = int(config['NAME']['NAME_WIDTH'])
			self.x2 = int(config['EVENT']['EVENT_X'])
			self.y2 = int(config['EVENT']['EVENT_y'])
			self.width2 = int(config['EVENT']['EVENT_WIDTH'])
			self.x3 = int(config['DATE']['DATE_X'])
			self.y3 = int(config['DATE']['DATE_Y'])
			self.width3 = int(config['DATE']['DATE_WIDTH'])
		except:
			print("\n!! ERORR : CHECK THE CONFIG FILE !!\n")
			return 0
		return 1

	def create(self):
		"""
		
		Creates the actual certificate with the configurations and inputs specified 
		and saves the output accordingly.

		"""
		if self.configure()==0:
			return 0
		try:
			image = Image.open(self.cert)
		except:
			print("\n!! ERROR : CHECK TEMPLATE FILE !!\n")
			return 0
		draw = ImageDraw.Draw(image)
		try:
			font1 = ImageFont.truetype(self.font1, size=self.size1)
			font2 = ImageFont.truetype(self.font2, size=self.size2)
			font3 = ImageFont.truetype(self.font3, size=self.size3)
		except:
			print("\n!! ERROR : CHECK FONT FILES !!\n")
			return 0
		width = font1.getsize(self.name)[0]
		draw.text((self.x1+(self.width1-width)/2, self.y1-self.size1), self.name, fill=self.color1, font=font1)
		width = font2.getsize(self.course)[0]
		draw.text((self.x2+(self.width2-width)/2, self.y2-self.size2), self.course, fill=self.color2, font=font2)
		width = font3.getsize(self.date)[0]
		draw.text((self.x3+(self.width3-width)/2, self.y3-self.size3), self.date, fill=self.color3, font=font3)
		try:
			image.save(self.output)
			print("\n>>  CERTIFICATE GENERATED AND SAVED AS : "+self.output+ "  <<\n")
		except:
			print("\n!! ERORR : CERTIFICATE COULD NOT BE SAVED !!\n")
			return 0
		return 1
