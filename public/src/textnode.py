from enum import Enum

class TextType(Enum):
	NORMAL = "normal"
	BOLD = "bold"
	ITALIC = "italic"
	CODE = "code"
	LINKS = "links"
	IMAGES = "images"
	
class TextNode():
	def __init__(self, text, text_type, url=None):
		self.text = text
		self.text_type = text_type
		self.url = url

	def __eq__(self, text_node):
		if (self.text == text_node.text and
			self.text_type == text_node.text_type and
			self.url == text_node.url):
			return True
		return False

	def __repr__(self):
		f_st = \
		f"TextNode(text = {self.text}, " \
		f"text type = {self.text_type.value}, " \
		f"url = {self.url})"
		return f_st
		
	    
        
        # f_str = \
        #     f"TextNode(text = {self.text}, " \ 
        #     f"text type = {self.text_type.value}, " \
        #     f"url = {self.url})"
		# return f_str
