class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError  

    def props_to_html(self):
        if self.props is None:
            return ""
        html_str = ""
        for prop in self.props:
            html_str += f' {prop}="{self.props[prop]}"'
        
        return html_str
    
    def __repr__(self):
        f_st = \
        f"HTMLNode(tag = {self.tag}, " \
        f"value = {self.value}, " \
        f"children = {self.children}, " \
        f"props = {self.props})"
        return f_st
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)    

    def to_html(self):
        if self.value == None:
            raise ValueError("leaf node must have value")
        if self.tag == None:
            return self.value
        if self.props == None:
            return f'<{self.tag}>{self.value}</{self.tag}>'    
        return f'<{self.tag}> {self.props_to_html}</{self.tag}>'
    
    def __repr__(self):
        f_st = \
        f"HTMLNode(tag = {self.tag}, " \
        f"value = {self.value}, " \
        f"props = {self.props})"
        return f_st
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("parent node must have tag")
        if self.children is None:
            raise ValueError("parent node must have children")
        str = ""
        for child in self.children:
            str += child.to_html()
        return f'<{self.tag}>{str}</{self.tag}>'
    
    def __repr__(self):
        f_st = \
        f"HTMLNode(tag = {self.tag}, " \
        f"children = {self.children}, " \
        f"props = {self.props})"
        return f_st