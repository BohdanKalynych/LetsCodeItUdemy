from sandbox_folder.header import Header
from sandbox_folder.footer import Footer

class Header_section(Header):

    def find_header_name_and_verify_in_header_section(self):
        self.get_header_value()

    def find_footer_size(self):
        self.footer = Footer()
        self.footer.get_footer_size()


a1 = Header_section()
a1.find_header_name_and_verify_in_header_section()
a1.find_footer_size()